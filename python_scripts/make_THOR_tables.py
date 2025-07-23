CREATE TABLE master (id NUMBER(10), Master_Index_Number(1000), Theater(50));
CREATE TABLE temporal (MsnDate STR(50), Day NUMBER(2), Month NUMBER(2), Year NUMBER(4), NAF STR(1000));
CREATE TABLE mission_data (Country_Flying_Mission STR(100), TGT_Country_Code STR(100), Country_Name STR(100), Location_Name STR(100), Target_Type_Description STR(100), Target_ID_Code STR(100), TGT_Industry_Code STR(100), Target_Industry_Description STR(100)):
CREATE TABLE course (Source_Lat NUMBER(50), Source_Lon NUMBER(50), Lat NUMBER(50), Lon NUMBER(50));
CREATE TABLE unit_info (Unit_ID NUMBER(20), MDS STR(50), Aircraft_name STR(50), Msn_Type STR(20), Target_Priority NUMBER(150), Target_priority_Explanation STR(150), Attacking_AC NUMBER(100));
CREATE TABLE altitude (Altitude NUMBER(50), Altitude_Feet NUMBER(50));
CREATE TABLE ordnance (Number_of_HE NUMBER(50), Type_of_HE STR(50), lbs_HE NUMBER(50), Tons_of_HE NUMBER(50), Number_of_IC NUMBER(50), Type_of_IC STR(50), lbs_IC NUMBER(50), Tons_of_IC NUMBER(50), Number_of_Frag NUMBER(50), Type_of_FRAG STR(50), lbs_Frag NUMBER(50), Tons_of_Frag NUMBER(50), Total_lbs NUMBER(50), TOTAL_TONS NUMBER(50));
CREATE TABLE departure (Source_Launch_Base STR(50), Source_Launch_Base_Country STR(50), Source_Launch_Base_Lat NUMBER(50), Source_Launch_Base_Long NUMBER(50), Sortie_Dupe STR(50));
CREATE TABLE aar (Total_AC_Lost NUMBER(50), Total_AC_Damaged NUMBER(50), Airborne_AC NUMBER(50), Number_of_AC_Dropping_Bombs NUMBER(50), Time_over_Target STR(50), Sighting_Method_Code STR(50), Sighting_Explanation STR(50), BDA STR(50), Speed NUMBER(50), Callsign STR(50), Rounds_Ammo NUMBER(50));
CREATE TABLE escorts (Number_Escort_Planes NUMBER(50), Type_of_Escort_Planes STR(50), Spares_Return_AC STR(50));
CREATE TABLE failures (WX_Fail_AC STR(50), Mech_Fail_AC STR(50), Misc_Fail_AC STR(50), Other_Fail_AC STR(50), TONS_LOST__JETTISONED NUMBER(50), GE_ICON_Color STR(50), GE_Color_Code STR(50), GE_icon STR(50), KML_Date STR(50), NAF_Color_Code STR(50));
CREATE TABLE comments (Target_Comment STR(50), Mission_Comments STR(50), Source STR(50), Database_Edit_Comments STR(50), Speed__MPH_ STR(50));