from google.cloud import bigquery, storage

def get_table(client):
    if tenant_id:
        sql = f"""
              YOUR SQL
              """
    df = client.query(sql).to_dataframe()
    return df
  
if __name__ == "__main__":
    
    storage_client = storage.Client()
    client = bigquery.Client()
    
    df = get_table(client)
