def preprocess():
    '''Prepares Keene PM 2.5 datafile for machine learning through trunkation
    and label encoding. Data is tuned to governmental BAM weather standards.
    '''

    # instantiate pathway variables
    projectDir = 'D:\mattp\Documents\School\SeniorYear\DataAnalysis'
    dataDir = projectDir + '\WaterStreetPA_WthrMETAR_SNOW-2018.csv'

    #read data into DataFrame
    data = pd.read_csv(dataDir,header=0)

    # process datetime
    import datetime as dt
    dtParsed = [0 for i in range(Data.shape[0])]
    for i in range(Data.shape[0]):
        dtParsed[i] = dt.datetime.strptime(Data.datetime.values[i], '%Y-%m-%d %H:%M:%S')

    # enumerate time of day
    dtEnumerated = [0 for i in range(Data.shape[0])]
    for i in range(Data.shape[0]):
        dtEnumerated[i] = dtParsed[i].hour*3600 + dtParsed[i].minute*60 + dtParsed[i].second
    dtEmumeratedDf = pd.DataFrame(dtEnumerated)

    # drop out bad rows
    Data.reset_index(drop=True, inplace=True)

    # combine features and output for scaling
    features = pd.concat([dtEmumeratedDf, Data.temp, Data.dewpoint, Data.RH,
                        Data.windDIR, Data.windMPH, Data.precip, Data.mslp,
                        Data.visibility, Data.gust, Data['(top) Snow Depth (in)'],
                        Data['(middle) Snow Depth (in)'], Data['(bottom) Snow Depth (in)'],
                        Data['(top) Snow Temp. (deg. F)'], Data['(middle) Snow Temp. (deg. F)'],
                        Data['(bottom) Snow Temp. (deg. F)'], Data['(top) Snow Density (%)'],
                        Data['(middle) Snow Density (%)'], Data['(bottom) Snow Density (%)'],
                        Data.FEW, Data.SCT, Data.BKN, Data.OVC, Data.VV, Data.Clouds,
                        Data.Clds1000, Data.Clds2000, Data.Clds3000, Data.Clds4000, Data.Clds5000,
                        Data.Clds6000, Data.Clds7000, Data.Clds8000, Data.Clds9000, Data.Clds10000],axis=1)
