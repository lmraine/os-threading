#IMPORTS HERE

#WRITE FUNCTION HERE

urls= ['https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD',
        'https://data.cityofnewyork.us/api/views/c3uy-2p5r/rows.csv?accessType=DOWNLOAD',
        'https://edg.epa.gov/EPADataCommons/public/OA/EPA_SmartLocationDatabase_V3_Jan_2021_Final.csv',
        'https://ecos.fws.gov/ServCat/DownloadFile/173741?Reference=117348',
        'https://data.nasa.gov/api/views/gh4g-9sfh/rows.csv?accessType=DOWNLOAD']

filenames = ['ElectricVehicleData.csv',
            'AirQualityData.csv',
            'WalkabilityIndex.csv',
            'WaterQualityData.csv',
            'MeteoriteLandings.csv']

#CREATE START THREADS HERE