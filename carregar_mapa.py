import geopandas as gpd
from pathlib import Path

def carregar_mapa():

    path_sf = Path(r'C:\Users\isabe\OneDrive\Documentos\Estudos\Projeto Python\Algoritmos em Grafos\bairros.geojson')
    
    if not path_sf.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {path_sf}")
    
    
    geo_df = gpd.read_file(path_sf)
    geo_df = geo_df.to_crs(epsg=31983)
    geo_df['centroide'] = geo_df.geometry.centroid
    geo_df['x'] = geo_df.centroide.x.round(2)
    geo_df['y'] = geo_df.centroide.y.round(2)
    geo_df = geo_df

    return geo_df

if __name__ == "__main__":
    df = carregar_mapa()
    print(df[['EBAIRRNOME', 'x', 'y']])
    print("Total de bairros:", len(df))
