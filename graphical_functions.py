# Funciones graficas

# Librearias

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

# Function 1
def graph(data):   

    for n, i in enumerate(data):
        plt.subplot(4, 3, n+1)

        if len(data[i].value_counts()) > 7 :

            plt.hist(data[i], alpha=.9, color='#00bcbc') 
            plt.axvline(np.mean(data[i]), label = 'Media',color = '#e94a4e', lw =4) 

            plt.title(i,fontsize = 30,fontweight='bold')

            #plt.ylabel('Frecuencia',fontsize = 25) 
            plt.xlabel("",fontsize = 20)

            plt.legend(fontsize = 25) 
            plt.xticks(fontsize=25)
            plt.yticks(fontsize=30)
            
            plt.subplots_adjust(wspace=0.5,hspace=0.8)

        else:
            sns.countplot(x=data[i], order=data[i].value_counts().index,
                          palette=['#d4ebfc', '#e94a4e','#00bcbc', '#0258a1'])
            
            plt.title(i,fontsize = 30,fontweight='bold')

            plt.xlabel("",fontsize = 20)
            plt.ylabel("",fontsize =20)
            #plt.ylabel('Cantidad',fontsize = 25)

            plt.tight_layout()

            plt.xticks(fontsize=25)
            plt.yticks(fontsize=30)

            plt.subplots_adjust(wspace=0.5,hspace=0.8)


# Function 2
def fetch_features(dataframe,v_objetivo):

    columns = dataframe.columns
    attr_name,pearson_r,abrs_pearson_r = [],[],[]

    for col in columns:
        if col !=v_objetivo: 
            attr_name.append(col)
            pearson_r.append(dataframe[col].corr(dataframe[v_objetivo]))
            abrs_pearson_r.append(abs(dataframe[col].corr(dataframe[v_objetivo]))) 

    features = pd.DataFrame(
        {'attribute':attr_name,
        'corr':pearson_r,
        'abs_corr': abrs_pearson_r}
    )
    features = (features.set_index('attribute')).round(3)
    return features.sort_values(by=['abs_corr'], ascending=False)