
# coding: utf-8

# In[2]:


import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
from shapely.geometry import Point


# In[3]:


dataset1 = pd.read_csv('dataset1_combined.csv', ',')


# In[4]:


dataset1['Coordinates'] = list(zip(dataset1.longitude, dataset1.latitude))

dataset1['Coordinates'] = dataset1['Coordinates'].apply(Point)

geofile1 = gpd.GeoDataFrame(dataset1, geometry='Coordinates')


# In[5]:


usa = gpd.read_file('tl_2018_us_state/tl_2018_us_state.shp')
coastline = gpd.read_file('tl_2018_us_coastline/tl_2018_us_coastline.shp')
rails = gpd.read_file('tl_2018_us_rails/tl_2018_us_rails.shp')
urban_zones = gpd.read_file('tl_2018_us_uac10/tl_2018_us_uac10.shp')


# In[6]:


california_lm = gpd.read_file('tl_2018_06_arealm/tl_2018_06_arealm.shp')
colorado_lm = gpd.read_file('tl_2018_08_arealm/tl_2018_08_arealm.shp')
dc_lm = gpd.read_file('tl_2018_11_arealm/tl_2018_11_arealm.shp')
idaho_lm = gpd.read_file('tl_2018_16_arealm/tl_2018_16_arealm.shp')
illinois_lm = gpd.read_file('tl_2018_17_arealm/tl_2018_17_arealm.shp')
indiana_lm = gpd.read_file('tl_2018_18_arealm/tl_2018_18_arealm.shp')
iowa_lm = gpd.read_file('tl_2018_19_arealm/tl_2018_19_arealm.shp')
kansas_lm = gpd.read_file('tl_2018_20_arealm/tl_2018_20_arealm.shp')
maryland_lm = gpd.read_file('tl_2018_24_arealm/tl_2018_24_arealm.shp')
minnesota_lm = gpd.read_file('tl_2018_27_arealm/tl_2018_27_arealm.shp')
montana_lm = gpd.read_file('tl_2018_30_arealm/tl_2018_30_arealm.shp')
nebraska_lm = gpd.read_file('tl_2018_31_arealm/tl_2018_31_arealm.shp')
nevada_lm = gpd.read_file('tl_2018_32_arealm/tl_2018_32_arealm.shp')
northdakota_lm = gpd.read_file('tl_2018_38_arealm/tl_2018_38_arealm.shp')
ohio_lm = gpd.read_file('tl_2018_39_arealm/tl_2018_39_arealm.shp')
oregon_lm = gpd.read_file('tl_2018_41_arealm/tl_2018_41_arealm.shp')
pennsylvania_lm = gpd.read_file('tl_2018_42_arealm/tl_2018_42_arealm.shp')
utah_lm = gpd.read_file('tl_2018_49_arealm/tl_2018_49_arealm.shp')
virginia_lm = gpd.read_file('tl_2018_51_arealm/tl_2018_51_arealm.shp')
washington_lm = gpd.read_file('tl_2018_53_arealm/tl_2018_53_arealm.shp')
westvirginia_lm = gpd.read_file('tl_2018_54_arealm/tl_2018_54_arealm.shp')
wisconsin_lm = gpd.read_file('tl_2018_55_arealm/tl_2018_55_arealm.shp')


# In[8]:


fig, ax = plt.subplots(figsize = (30,30))
ax.set_xlim([-126, -66])
ax.set_ylim([23, 51])

usa.plot(ax = ax, color='white', edgecolor='black')
coastline.plot(ax = ax)
rails.plot(ax = ax, alpha = 0.4)
#urban_zones.plot(ax = ax, color='green', edgecolor='green', alpha = 0.3)
#cali_landmarks.plot(ax = ax, color = 'orange')
#lm1.plot(ax = ax, color = 'orange', alpha = 0.5)

geofile1.plot(ax=ax, color='blue')

plt.title('Geolocation Map of Cross-Country Trip', fontsize=48)
plt.xlabel('Longitude', fontsize=36)
plt.ylabel('Latitude', fontsize=36)
plt.tick_params(axis='both', which='major', labelsize=32)
plt.tick_params(axis='both', which='minor', labelsize=32)
plt.show()


# In[9]:


fig, ax = plt.subplots(figsize = (30,30))
ax.set_xlim([-88, -76])
ax.set_ylim([37, 50])

usa.plot(ax = ax, color='white', edgecolor='black')
coastline.plot(ax = ax)
rails.plot(ax = ax, alpha = 0.4)

virginia_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
maryland_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
dc_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
pennsylvania_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
westvirginia_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
ohio_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
indiana_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
wisconsin_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
illinois_lm.plot(ax = ax, color = 'orange', alpha = 0.7)

geofile1.plot(ax=ax, color='blue')

plt.title('Geolocation Map of Cross-Country Trip - View 4', fontsize=42)
plt.xlabel('Longitude', fontsize=36)
plt.ylabel('Latitude', fontsize=36)
plt.tick_params(axis='both', which='major', labelsize=32)
plt.tick_params(axis='both', which='minor', labelsize=32)
plt.minorticks_on()
plt.grid(True, 'both', 'both')
plt.show()


# In[10]:


fig, ax = plt.subplots(figsize = (30,30))
ax.set_xlim([-100, -88])
ax.set_ylim([37, 50])

usa.plot(ax = ax, color='white', edgecolor='black')
coastline.plot(ax = ax)
rails.plot(ax = ax, alpha = 0.4)

wisconsin_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
minnesota_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
northdakota_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
iowa_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
nebraska_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
illinois_lm.plot(ax = ax, color = 'orange', alpha = 0.7)

geofile1.plot(ax=ax, color='blue')

plt.title('Geolocation Map of Cross-Country Trip - View 3', fontsize=42)
plt.xlabel('Longitude', fontsize=36)
plt.ylabel('Latitude', fontsize=36)
plt.tick_params(axis='both', which='major', labelsize=32)
plt.tick_params(axis='both', which='minor', labelsize=32)
plt.minorticks_on()
plt.grid(True, 'both', 'both')
plt.show()


# In[11]:


fig, ax = plt.subplots(figsize = (30,30))
ax.set_xlim([-112, -100])
ax.set_ylim([37, 50])

usa.plot(ax = ax, color='white', edgecolor='black')
coastline.plot(ax = ax)
rails.plot(ax = ax, alpha = 0.4)

northdakota_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
montana_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
utah_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
colorado_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
nebraska_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
kansas_lm.plot(ax = ax, color = 'orange', alpha = 0.7)

geofile1.plot(ax=ax, color='blue')

plt.title('Geolocation Map of Cross-Country Trip - View 2', fontsize=42)
plt.xlabel('Longitude', fontsize=36)
plt.ylabel('Latitude', fontsize=36)
plt.tick_params(axis='both', which='major', labelsize=32)
plt.tick_params(axis='both', which='minor', labelsize=32)
plt.minorticks_on()
plt.grid(True, 'both', 'both')
plt.show()


# In[12]:


fig, ax = plt.subplots(figsize = (30,30))
ax.set_xlim([-124, -112])
ax.set_ylim([37, 50])

usa.plot(ax = ax, color='white', edgecolor='black')
coastline.plot(ax = ax)
rails.plot(ax = ax, alpha = 0.4)

montana_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
idaho_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
washington_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
oregon_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
california_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
nevada_lm.plot(ax = ax, color = 'orange', alpha = 0.7)
utah_lm.plot(ax = ax, color = 'orange', alpha = 0.7)

geofile1.plot(ax=ax, color='blue')

plt.title('Geolocation Map of Cross-Country Trip - View 1', fontsize=42)
plt.xlabel('Longitude', fontsize=36)
plt.ylabel('Latitude', fontsize=36)
plt.tick_params(axis='both', which='major', labelsize=32)
plt.tick_params(axis='both', which='minor', labelsize=32)
plt.minorticks_on()
plt.grid(True, 'both', 'both')
plt.show()

