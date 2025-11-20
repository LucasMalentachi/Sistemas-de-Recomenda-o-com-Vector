import chromadb

def main():
    print("--- DIAGNÓSTICO COMPLETO ---")
    chroma_client = chromadb.Client()
    

    try:
        chroma_client.delete_collection(name="debug_cinema")
    except:
        pass

    collection = chroma_client.create_collection(name="debug_cinema")

    
    sinopses = [
        "Machines control humanity matrix.",            # Matrix
        "Toys come to life woody buzz.",                # Toy Story
        "Clown killer horror scary fear terror.",       # It
        "Ship sinking romance love titanic.",           # Titanic
        "Space war laser fights star wars."             # Star Wars
    ]
    titulos = ["Matrix", "Toy Story", "It (O Palhaço)", "Titanic", "Star Wars"]
    ids = ["id1", "id2", "id3", "id4", "id5"]

    collection.add(documents=sinopses, metadatas=[{"titulo": t} for t in titulos], ids=ids)

    
    query = "scary movie fear"
    print(f"\n🔎 Pergunta: '{query}'")
    
    
    resultados = collection.query(
        query_texts=[query],
        n_results=5 
    )

    print("\n--- RANKING DE RELEVÂNCIA ---")
   
    titulos_retornados = resultados['metadatas'][0]
    distancias = resultados['distances'][0]

    for i in range(len(titulos_retornados)):
        titulo = titulos_retornados[i]['titulo']
        nota = distancias[i]
        print(f"{i+1}º Lugar: {titulo} (Distância: {nota:.4f})")

if __name__ == "__main__":
    main()