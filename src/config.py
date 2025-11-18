import os 


class Config:
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    DATA_DIR = os.path.join(PROJECT_ROOT, 'artifacts', 'data')
    RAW_DATA_DIR = os.path.join(PROJECT_ROOT, 'artifacts', 'data', 'raw')
    PROCESSED_DATA_DIR = os.path.join(PROJECT_ROOT, 'artifacts', 'data', 'processed')
    MODEL_DIR = os.path.join(PROJECT_ROOT, 'artifacts', 'models')
    RESULTS_DIR = os.path.join(PROJECT_ROOT, 'artifacts', 'results')
    METADATA_FILE = os.path.join(PROJECT_ROOT, 'artifacts', 'data', 'metadata.json')
    CLASS_NAMES = ['Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy',
                   'Potato___Early_blight', 'Potato___healthy', 'Potato___Late_blight', 
                   'Tomato__Target_Spot', 'Tomato__Tomato_mosaic_virus', 'Tomato__Tomato_YellowLeaf__Curl_Virus',
                   'Tomato_Bacterial_spot','Tomato_Early_blight', 'Tomato_healthy', 'Tomato_Late_blight', 
                   'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot', 'Tomato_Spider_mites_Two_spotted_spider_mite'
                    
                   ]
  