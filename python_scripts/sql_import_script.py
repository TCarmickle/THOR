import csv
import oracledb
print("THOR DATABASE STRIPPER")

connection = oracledb.connect(
    user="your_username",
    password="your_password",
    dsn="localhost/dbxpdb"  # Example: "localhost/orclpdb"
)

STRINGSORT = input("Enter thing to sort for: ")

#FILENAME = input("Enter Filename of CSV file to Analyze: ")
FILENAME = "THOR_WW2_7_31_2013"
OUTFILE = FILENAME + "_" + STRINGSORT + ".csv"
INPUTFILE = FILENAME + ".csv"

out_file = open(OUTFILE, "w")

out_file.write("id,Master_Index_Number,Theater,MsnDate,Day,Month,Year,NAF,Country_Flying_Mission,TGT_Country_Code,Country_Name,Location_Name,Target_Type_Description,Target_ID_Code,TGT_Industry_Code,Target_Industry_Description,Source_Lat,Source_Lon,Lat,Lon,Unit_ID,MDS,Aircraft_name,Msn_Type,Target_Priority,Target_priority_Explanation,Attacking_AC,Altitude,Altitude_Feet,Number_of_HE,Type_of_HE,lbs_HE,Tons_of_HE,Number_of_IC,Type_of_IC,lbs_IC,Tons_of_IC,Number_of_Frag,Type_of_FRAG,lbs_Frag,Tons_of_Frag,Total_lbs,TOTAL_TONS,Source_Launch_Base,Source_Launch_Base_Country,Source_Launch_Base_Lat,Source_Launch_Base_Long,Sortie_Dupe,Total_AC_Lost,Total_AC_Damaged,Airborne_AC,Number_of_AC_Dropping_Bombs,Time_over_Target,Sighting_Method_Code,Sighting_Explanation,BDA,Speed,Callsign,Rounds_Ammo,Number_Escort_Planes,Type_of_Escort_Planes,Spares_Return_AC,WX_Fail_AC,Mech_Fail_AC,Misc_Fail_AC,Other_Fail_AC,TONS_LOST__JETTISONED,GE_ICON_Color,GE_Color_Code,GE_icon,KML_Date,NAF_Color_Code,Target_Comment,Mission_Comments,Source,Database_Edit_Comments,Speed__MPH_" + '\n')

with open (INPUTFILE) as ClassFile:
    reader = csv.DictReader(ClassFile)
    for row in reader:
        MAINID = str(row["id"])
        Master_Index_Number = str(row["Master_Index_Number"])
        Theater = str(row["Theater"])
        MsnDate = str(row["MsnDate"])
        Day = str(row["Day"])
        Month = str(row["Month"])
        Year = str(row["Year"])
        NAF = str(row["NAF"])
        Country_Flying_Mission = str(row["Country_Flying_Mission"])
        TGT_Country_Code = str(row["TGT_Country_Code"])
        Country_Name = str(row["Country_Name"])
        Location_Name = str(row["Location_Name"])
        Target_Type_Description = str(row["Target_Type_Description"])
        Target_ID_Code = str(row["Target_ID_Code"])
        TGT_Industry_Code = str(row["TGT_Industry_Code"])
        Target_Industry_Description = str(row["Target_Industry_Description"])
        Source_Lat = str(row["Source_Lat"])
        Source_Lon = str(row["Source_Lon"])
        Lat = str(row["Lat"])
        Lon = str(row["Lon"])
        Unit_ID = str(row["Unit_ID"])
        MDS = str(row["MDS"])
        Aircraft_name = str(row["Aircraft_name"])
        Msn_Type = str(row["Msn_Type"])
        Target_Priority = str(row["Target_Priority"])
        Target_priority_Explanation = str(row["Target_priority_Explanation"])
        Attacking_AC = str(row["Attacking_AC"])
        Altitude = str(row["Altitude"])
        Altitude_Feet = str(row["Altitude_Feet"])
        Number_of_HE = str(row["Number_of_HE"])
        Type_of_HE = str(row["Type_of_HE"])
        lbs_HE = str(row["lbs_HE"])
        Tons_of_HE = str(row["Tons_of_HE"])
        Number_of_IC = str(row["Number_of_IC"])
        Type_of_IC = str(row["Type_of_IC"])
        lbs_IC = str(row["lbs_IC"])
        Tons_of_IC = str(row["Tons_of_IC"])
        Number_of_Frag = str(row["Number_of_Frag"])
        Type_of_FRAG = str(row["Type_of_FRAG"])
        lbs_Frag = str(row["lbs_Frag"])
        Tons_of_Frag = str(row["Tons_of_Frag"])
        Total_lbs = str(row["Total_lbs"])
        TOTAL_TONS = str(row["TOTAL_TONS"])
        Source_Launch_Base = str(row["Source_Launch_Base"])
        Source_Launch_Base_Country = str(row["Source_Launch_Base_Country"])
        Source_Launch_Base_Lat = str(row["Source_Launch_Base_Lat"])
        Source_Launch_Base_Long = str(row["Source_Launch_Base_Long"])
        Sortie_Dupe = str(row["Sortie_Dupe"])
        Total_AC_Lost = str(row["Total_AC_Lost"])
        Total_AC_Damaged = str(row["Total_AC_Damaged"])
        Airborne_AC = str(row["Airborne_AC"])
        Number_of_AC_Dropping_Bombs = str(row["Number_of_AC_Dropping_Bombs"])
        Time_over_Target = str(row["Time_over_Target"])
        Sighting_Method_Code = str(row["Sighting_Method_Code"])
        Sighting_Explanation = str(row["Sighting_Explanation"])
        BDA = str(row["BDA"])
        Speed = str(row["Speed"])
        Callsign = str(row["Callsign"])
        Rounds_Ammo = str(row["Rounds_Ammo"])
        Number_Escort_Planes = str(row["Number_Escort_Planes"])
        Type_of_Escort_Planes = str(row["Type_of_Escort_Planes"])
        Spares_Return_AC = str(row["Spares_Return_AC"])
        WX_Fail_AC = str(row["WX_Fail_AC"])
        Mech_Fail_AC = str(row["Mech_Fail_AC"])
        Misc_Fail_AC = str(row["Misc_Fail_AC"])
        Other_Fail_AC = str(row["Other_Fail_AC"])
        TONS_LOST__JETTISONED = str(row["TONS_LOST__JETTISONED"])
        GE_ICON_Color = str(row["GE_ICON_Color"])
        GE_Color_Code = str(row["GE_Color_Code"])
        GE_icon = str(row["GE_icon"])
        KML_Date = str(row["KML_Date"])
        NAF_Color_Code = str(row["NAF_Color_Code"])
        Target_Comment = str(row["Target_Comment"])
        Mission_Comments = str(row["Mission_Comments"])
        Source = str(row["Source"])
        Database_Edit_Comments = str(row["Database_Edit_Comments"])
        Speed__MPH_ = str(row["Speed__MPH_"])

        try:
            cursor = connection.cursor()

            insert_query_master = """
            INSERT INTO master (id, master_index_number, theater)
            VALUES (:1, :2, :3)
            """
            insert_query_temporal = """
            INSERT INTO temporal (MsnDate, Day, Month, Year, NAF)
            VALUES (:1, :2, :3, :4, :5)
            """
            insert_query_mission_data = """
            INSERT INTO mission_data (Country_Flying_Mission, TGT_Country_Code, Country_Name, Location_Name, Target_Type_Description, Target_ID_Code, TGT_Industry_Code, Target_Industry_Description)
            VALUES (:1, :2, :3, :4, :5, :6, :7, :8)
            """
            insert_query_course = """
            INSERT INTO course (Source_Lat, Source_Lon, Lat, Lon)
            VALUES (:1, :2, :3, :4)
            """
            insert_query_unit_info = """
            INSERT INTO unit_info (Unit_ID, MDS, Aircraft_name, Msn_Type, Target_Priority, Target_priority_Explanation, Attacking_AC)
            VALUES (:1, :2, :3, :4, :5, :6, :7)
            """
            insert_query_altitude = """
            INSERT INTO altitude (Altitude, Altitude_Feet)
            VALUES (:1, :2)
            """
            insert_query_ordnance = """
            INSERT INTO ordnance (Number_of_HE, Type_of_HE, lbs_HE, Tons_of_HE, Number_of_IC, Type_of_IC, lbs_IC, Tons_of_IC, Number_of_Frag, Type_of_FRAG, lbs_Frag, Tons_of_Frag, Total_lbs, TOTAL_TONS)
            VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14)
            """
            insert_query_departure = """
            INSERT INTO departure (Source_Launch_Base, Source_Launch_Base_Country, Source_Launch_Base_Lat, Source_Launch_Base_Long, Sortie_Dupe)
            VALUES (:1, :2, :3, :4, :5)
            """
            insert_query_aar = """
            INSERT INTO aar (Total_AC_Lost, Total_AC_Damaged, Airborne_AC, Number_of_AC_Dropping_Bombs, Time_over_Target, Sighting_Method_Code, Sighting_Explanation, BDA, Speed, Callsign, Rounds_Ammo)
            VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11)
            """
            insert_query_escorts = """
            INSERT INTO escorts (Number_Escort_Planes, Type_of_Escort_Planes, Spares_Return_AC)
            VALUES (:1, :2, :3)
            """
            insert_query_failures = """
            INSERT INTO failures (WX_Fail_AC, Mech_Fail_AC, Misc_Fail_AC, Other_Fail_AC, TONS_LOST__JETTISONED, GE_ICON_Color, GE_Color_Code, GE_icon, KML_Date, NAF_Color_Code)
            VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10)
            """
            insert_query_comments = """
            INSERT INTO comments (Target_Comment, Mission_Comments, Source, Database_Edit_Comments, Speed__MPH_)
            VALUES (:1, :2, :3, :4, :5)
            """
            data_to_insert_master = (MAINID, Master_Index_Number, Theater)
            data_to_insert_temporal = (MsnDate, Day, Month, Year, NAF)
            data_to_insert_mission_data = (Country_Flying_Mission, TGT_Country_Code, Country_Name, Location_Name, Target_Type_Description, Target_ID_Code, TGT_Industry_Code, Target_Industry_Description)
            data_to_insert_course = (Source_Lat, Source_Lon, Lat, Lon)
            data_to_insert_unit_info = (Unit_ID, MDS, Aircraft_name, Msn_Type, Target_Priority, Target_priority_Explanation, Attacking_AC)
            data_to_insert_altitude = (Altitude, Altitude_Feet)
            data_to_insert_ordnance = (Number_of_HE, Type_of_HE, lbs_HE, Tons_of_HE, Number_of_IC, Type_of_IC, lbs_IC, Tons_of_IC, Number_of_Frag, Type_of_FRAG, lbs_Frag, Tons_of_Frag, Total_lbs, TOTAL_TONS)
            data_to_insert_aar = (Total_AC_Lost, Total_AC_Damaged, Airborne_AC, Number_of_AC_Dropping_Bombs, Time_over_Target, Sighting_Method_Code, Sighting_Explanation, BDA, Speed, Callsign, Rounds_Ammo)
            data_to_insert_escorts = (Type_of_Escort_Planes, Spares_Return_AC)
            data_to_insert_failures = (WX_Fail_AC, Mech_Fail_AC, Misc_Fail_AC, Other_Fail_AC, TONS_LOST__JETTISONED, GE_ICON_Color, GE_Color_Code, GE_icon, KML_Date, NAF_Color_Code)
            data_to_insert_comments = (Target_Comment, Mission_Comments, Source, Database_Edit_Comments, Speed__MPH_)

            cursor.execute(insert_query_master, data_to_insert_master)
            cursor.execute(insert_query_temporal, data_to_insert_temporal)
            cursor.execute(insert_query_mission_data, data_to_insert_mission_data)
            cursor.execute(insert_query_course, data_to_insert_course)
            cursor.execute(insert_query_unit_info, data_to_insert_unit_info)
            cursor.execute(insert_query_altitude, data_to_insert_altitude)
            cursor.execute(insert_query_ordnance, data_to_insert_ordnance)
            cursor.execute(insert_query_aar, data_to_insert_aar)
            cursor.execute(insert_query_escorts, data_to_insert_escorts)
            cursor.execute(insert_query_failures, data_to_insert_failures)
            cursor.execute(insert_query_comments, data_to_insert_comments)
           

            connection.commit()

        except oracledb.DatabaseError as e:
            # Handle any database errors
            print("Error occurred:", e)

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()

        

out_file.close()
#input ("HOLDING...")