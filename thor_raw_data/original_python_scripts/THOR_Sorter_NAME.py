import csv
print("THOR DATABASE STRIPPER")
LOCATIONSORTER1 = input("Enter FIRST location to sort for: ")
LOCATIONSORTER2 = input("Enter SECOND location to sort for: ")

#FILENAME = input("Enter Filename of CSV file to Analyze: ")
FILENAME = "THOR_WW2_7_31_2013"
OUTFILE = FILENAME + "_" + LOCATIONSORTER1 + ".csv"
INPUTFILE = FILENAME + ".csv"

out_file = open(OUTFILE, "w")

out_file.write("id,Master_Index_Number,Theater,MsnDate,Day,Month,Year,NAF,Country_Flying_Mission,TGT_Country_Code,Country_Name,Location_Name,Target_Type_Description,Target_ID_Code,TGT_Industry_Code,Target_Industry_Description,Source_Lat,Source_Lon,Lat,Lon,Unit_ID,MDS,Aircraft_name,Msn_Type,Target_Priority,Target_priority_Explanation,Attacking_AC,Altitude,Altitude_Feet,Number_of_HE,Type_of_HE,lbs_HE,Tons_of_HE,Number_of_IC,Type_of_IC,lbs_IC,Tons_of_IC,Number_of_Frag,Type_of_FRAG,lbs_Frag,Tons_of_Frag,Total_lbs,TOTAL_TONS,Source_Launch_Base,Source_Launch_Base_Country,Source_Launch_Base_Lat,Source_Launch_Base_Long,Sortie_Dupe,Total_AC_Lost,Total_AC_Damaged,Airborne_AC,Number_of_AC_Dropping_Bombs,Time_over_Target,Sighting_Method_Code,Sighting_Explanation,BDA,Speed,Callsign,Rounds_Ammo,#_Escort_Planes,Type_of_Escort_Planes,Spares_Return_AC,WX_Fail_AC,Mech_Fail_AC,Misc_Fail_AC,Other_Fail_AC,TONS_LOST__JETTISONED,GE_ICON_Color,GE_Color_Code,GE_icon,KML_Date,NAF_Color_Code,Target_Comment,Mission_Comments,Source,Database_Edit_Comments,Speed__MPH_" + '\n')

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
        Escort_Planes = str(row["#_Escort_Planes"])
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

        if (Country_Name == LOCATIONSORTER1) or (Country_Name == LOCATIONSORTER2):
            #If we match this, do this:
            out_file.write(
                MAINID + "," +
                Master_Index_Number + "," +
                Theater + "," +
                MsnDate + "," +
                Day + "," +
                Month + "," +
                Year + "," +
                NAF + "," +
                Country_Flying_Mission + "," +
                TGT_Country_Code + "," +
                Country_Name + "," +
                Location_Name + "," +
                Target_Type_Description + "," +
                Target_ID_Code + "," +
                TGT_Industry_Code + "," +
                Target_Industry_Description + "," +
                Source_Lat + "," +
                Source_Lon + "," +
                Lat + "," +
                Lon + "," +
                Unit_ID + "," +
                MDS + "," +
                Aircraft_name + "," +
                Msn_Type + "," +
                Target_Priority + "," +
                Target_priority_Explanation + "," +
                Attacking_AC + "," +
                Altitude + "," +
                Altitude_Feet + "," +
                Number_of_HE + "," +
                Type_of_HE + "," +
                lbs_HE + "," +
                Tons_of_HE + "," +
                Number_of_IC + "," +
                Type_of_IC + "," +
                lbs_IC + "," +
                Tons_of_IC + "," +
                Number_of_Frag + "," +
                Type_of_FRAG + "," +
                lbs_Frag + "," +
                Tons_of_Frag + "," +
                Total_lbs + "," +
                TOTAL_TONS + "," +
                Source_Launch_Base + "," +
                Source_Launch_Base_Country + "," +
                Source_Launch_Base_Lat + "," +
                Source_Launch_Base_Long + "," +
                Sortie_Dupe + "," +
                Total_AC_Lost + "," +
                Total_AC_Damaged + "," +
                Airborne_AC + "," +
                Number_of_AC_Dropping_Bombs + "," +
                Time_over_Target + "," +
                Sighting_Method_Code + "," +
                Sighting_Explanation + "," +
                BDA + "," +
                Speed + "," +
                Callsign + "," +
                Rounds_Ammo + "," +
                Escort_Planes + "," +
                Type_of_Escort_Planes + "," +
                Spares_Return_AC + "," +
                WX_Fail_AC + "," +
                Mech_Fail_AC + "," +
                Misc_Fail_AC + "," +
                Other_Fail_AC + "," +
                TONS_LOST__JETTISONED + "," +
                GE_ICON_Color + "," +
                GE_Color_Code + "," +
                GE_icon + "," +
                KML_Date + "," +
                NAF_Color_Code + "," +
                Target_Comment + "," +
                Mission_Comments + "," +
                Source + "," +
                Database_Edit_Comments + "," +
                Speed__MPH_ + '\n')

out_file.close()
print("DONE!")
#input ("HOLDING...")
