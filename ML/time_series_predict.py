import tensorflow as tf
from numpy import array
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from tensorflow.keras import optimizers
from xgboost import XGBClassifier, XGBRegressor
from lightgbm import LGBMClassifier, LGBMRegressor

## setting
target = '__y변수__' 
model = 'LSTM'

# 0. 데이터 로드 : 일별(행), 변수별(열) 형태의 시계열 데이터
df = pd.read_csv(f'__sample__.csv',encoding='euc-kr')

## 일별 데이터 T-1 ~ T-5 시점까지 변수화
def daily_linear_full(df,target, cols, lags=5):
    df = df.reset_index(drop=True)
    temp = df[['__DATE__']]
    for i in range(0,lags+1):
        temp[f'{target}_T-{i}'] = df[target][i:].reset_index(drop=True)
    new_cols = list(set(cols)-set(['__DATE__']))
    for col in new_cols:
        for i in range(1,lags+1):
            temp[f'{col}_T-{i}'] = df[col][i:].reset_index(drop=True)
    temp = temp[:-lags]
    return temp

lag_data = daily_linear_full(df, target, df.columns, lags=5) # new_df

X = lag_data.drop(columns=[target,'__DATE__'])
y = lag_data[target]

train_X = X[:-len(X)//5] # 80% 학습
valid_X = X[-len(X)//5:] # 20% 검증
train_y = y[:-len(X)//5] # 80% 학습
valid_y = y[-len(X)//5:] # 20% 검증

######### 예측 모델 구성 ###########
if model == 'LSTM':
    ########################### LSTM 기반 ##################################
    # 1. 데이터
    x = np.array(train_X.fillna(0)).reshape((train_X.shape[0],train_X.shape[1],1))
    y = np.array(train_y)

    # 2. 모델 구성
    model = Sequential()
    #model.add(LSTM(100, activation = 'elu', input_shape=(train_X.shape[1],1), return_sequences=True))
    model.add(LSTM(100, activation = 'elu', input_shape=(train_X.shape[1],1)))
    model.add(Dense(70, activation = 'elu'))
    model.add(Dense(50, activation = 'elu'))
    model.add(Dense(30, activation = 'elu'))
    model.add(Dense(15, activation = 'elu'))
    model.add(Dense(6))
    model.add(Dense(1))

    #model.summary()
    callback = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=40, mode = 'auto')
    # 3. 실행
    model.compile(optimizer=optimizers.Adam(lr=2e-3), loss='mse')
    hist = model.fit(x, y, epochs=400, batch_size=64,verbose=2, callbacks=[callback])

    x_input = np.array(valid_X).reshape((valid_X.shape[0],valid_X.shape[1],1))

    # 4. 최종 예측값
    yhat = model.predict(tf.cast(x_input, dtype='float64')) 
    #print(yhat)
    
else:
    ########################### Boosting 기반 ##################################

    # 1. 데이터
    x = train_X
    y = train_y

    # 2. 모델 구성 및 학습
    model = LGBMRegressor(n_estimators = 5000,
                          random_state = 420)
    model.fit(x, y, verbose=50, eval_set = [(valid_x, valid_y)], eval_metric = 'rmse', early_stopping_rounds=100)
    
    # 3. 최종 예측값
    yhat = model.predict(valid_x)
