import re

loc_str = """
Name: Alabama
Capital Name: Montgomery, AL

Capital Latitude: 32.361538

Capital Longitude: -86.279118



Name: Arizona

Capital Name: Phoenix, AZ

Capital Latitude: 33.448457

Capital Longitude: -112.073844

Name: Arkansas

Capital Name: Little Rock, AR

Capital Latitude: 34.736009

Capital Longitude: -92.331122

Name: California

Capital Name: Sacramento, CA

Capital Latitude: 38.555605

Capital Longitude: -121.468926

Name: Colorado

Capital Name: Denver, CO

Capital Latitude: 39.7391667

Capital Longitude: -104.984167

Name: Connecticut

Capital Name: Hartford, CT

Capital Latitude: 41.767

Capital Longitude: -72.677

Name: Delaware

Capital Name: Dover, DE

Capital Latitude: 39.161921

Capital Longitude: -75.526755

Name: Florida

Capital Name: Tallahassee, FL

Capital Latitude: 30.4518

Capital Longitude: -84.27277

Name: Georgia

Capital Name: Atlanta, GA

Capital Latitude: 33.76

Capital Longitude: -84.39


Name: Idaho

Capital Name: Boise, ID

Capital Latitude: 43.613739

Capital Longitude: -116.237651

Name: Illinois

Capital Name: Springfield, IL

Capital Latitude: 39.783250

Capital Longitude: -89.650373


Name: Iowa

Capital Name: Des Moines, IA

Capital Latitude: 41.590939

Capital Longitude: -93.620866

Name: Kansas

Capital Name: Topeka, KS

Capital Latitude: 39.04

Capital Longitude: -95.69

Name: Kentucky

Capital Name: Frankfort, KY

Capital Latitude: 38.197274

Capital Longitude: -84.86311

Name: Louisiana

Capital Name: Baton Rouge, LA

Capital Latitude: 30.45809

Capital Longitude: -91.140229

Name: Maine

Capital Name: Augusta, GA

Capital Latitude: 44.323535

Capital Longitude: -69.765261

Name: Maryland

Capital Name: Annapolis, MD

Capital Latitude: 38.972945

Capital Longitude: -76.501157

Name: Michigan

Capital Name: Lansing, MI

Capital Latitude: 42.7335

Capital Longitude: -84.5467

Name: Minnesota

Capital Name: Saint Paul, MN

Capital Latitude: 44.95

Capital Longitude: -93.094



Name: Missouri

Capital Name: Jefferson City, MO

Capital Latitude: 38.572954

Capital Longitude: -92.189283


Name: Nebraska

Capital Name: Lincoln, NE

Capital Latitude: 40.809868

Capital Longitude: -96.675345

Name: Nevada

Capital Name: Carson City, NV

Capital Latitude: 39.160949

Capital Longitude: -119.753877

Name: New Hampshire

Capital Name: Concord, NH

Capital Latitude: 43.220093

Capital Longitude: -71.549127

Name: New Jersey

Capital Name: Trenton, NJ

Capital Latitude: 40.221741

Capital Longitude: -74.756138

Name: New Mexico

Capital Name: Santa Fe, NM

Capital Latitude: 35.667231

Capital Longitude: -105.964575

Name: New York

Capital Name: Albany, NY

Capital Latitude: 42.659829

Capital Longitude: -73.781339

Name: North Carolina

Capital Name: Raleigh, NC

Capital Latitude: 35.771

Capital Longitude: -78.638

Name: North Dakota

Capital Name: Bismarck, ND

Capital Latitude: 48.813343

Capital Longitude: -100.779004

Name: Ohio

Capital Name: Columbus, OH

Capital Latitude: 39.962245

Capital Longitude: -83.000647

Name: Oklahoma

Capital Name: Oklahoma City, OK

Capital Latitude: 35.482309

Capital Longitude: -97.534994

Name: Oregon

Capital Name: Salem, OR

Capital Latitude: 44.931109

Capital Longitude: -123.029159


Name: Rhode Island

Capital Name: Providence, RI

Capital Latitude: 41.82355

Capital Longitude: -71.422132

Name: South Carolina

Capital Name: Columbia, SC

Capital Latitude: 34.000

Capital Longitude: -81.035

Name: South Dakota

Capital Name: Pierre, SD

Capital Latitude: 44.367966

Capital Longitude: -100.336378

Name: Tennessee

Capital Name: Nashville, TN

Capital Latitude: 36.165

Capital Longitude: -86.784

Name: Texas

Capital Name: Austin, TX

Capital Latitude: 30.266667

Capital Longitude: -97.75

Name: Utah

Capital Name: Salt Lake City, UT

Capital Latitude: 40.7547

Capital Longitude: -111.892622

Name: Vermont

Capital Name: Montpelier, VT

Capital Latitude: 44.26639

Capital Longitude: -72.57194

Name: Virginia

Capital Name: Richmond, VA

Capital Latitude: 37.54

Capital Longitude: -77.46

Name: Washington

Capital Name: Seattle, WA

Capital Latitude: 47.606209

Capital Longitude: -122.332069

Name: West Virginia

Capital Name: Charleston, WV

Capital Latitude: 38.349497

Capital Longitude: -81.633294

Name: Wisconsin

Capital Name: Madison, WI

Capital Latitude: 43.074722

Capital Longitude: -89.384444

Name: Wyoming

Capital Name: Cheyenne, WY

Capital Latitude: 41.145548

Capital Longitude: -104.802042
"""

pattern_name = "Capital Name: (.*?)\n"
re_name = re.compile(pattern_name, re.S)
capital_name = re_name.findall(loc_str)
print(capital_name)

pattern_lon = "Capital Longitude: (.*?)\n"
re_lon = re.compile(pattern_lon, re.S)
capital_lon = re_lon.findall(loc_str)
print(capital_lon)

pattern_lat = "Capital Latitude: (.*?)\n"
re_lat = re.compile(pattern_lat, re.S)
capital_lat = re_lat.findall(loc_str)
print(capital_lat)

print()
loc_dict = dict()
for i in range(len(capital_name)):
    lon = float(capital_lon[i])
    lat = float(capital_lat[i])
    loc_dict[capital_name[i]] = [lon, lat]

print(loc_dict)
