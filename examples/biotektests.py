import murraylab_tools.biotek as mt_biotek
import os
gitexamplepath =".\\examples\\biotek_examples\\"
data_filename = gitexamplepath+\
                "180515_big384wellplate.csv"
supplementary_filename = gitexamplepath+\
                "supp_inductiongrid.csv"

mt_biotek.tidy_biotek_data(data_filename, supplementary_filename, convert_to_uM = False)

import pandas as pd

tidy_filename = gitexamplepath+"180515_big384wellplate_tidy.csv"
df = pd.read_csv(tidy_filename)
df.loc[df.Excitation==580,"Channel"] = "RFP"
df.loc[df.Excitation==485,"Channel"] = "GFP"
#df.head()
#df.head()
#gdf = df.groupby(["Channel", "Gain", "Well"])
#gdf.head()
#df[df.Channel == "GFP"].head()
normdf = mt_biotek.normalize(df,norm_channel= "OD")
normdf.columns
import seaborn as sns
calcdf = mt_biotek.applyFunc(normdf,("GFP","RFP"),lambda x:x[0]/(x[0]+x[1]))
calcdf.head()
normdf[normdf.Channel=="RFP"].head()
normdf[normdf.Channel=="OD"].head()


cdf = mt_biotek.applyFunc()
#normdf[normdf.Gain==100].head()
end_df = mt_biotek.window_averages(normdf,15,17,"hours")

end_df.Excitation.unique()
slicedf = end_df[(end_df.Gain == 100 )&(end_df.Construct=="pQi41")&(end_df.aTC==250)]
end_df[(end_df.Gain == 100 )&(end_df.Construct=="pQi41")&(end_df.aTC==250)].head()
