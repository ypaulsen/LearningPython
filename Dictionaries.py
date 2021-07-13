# Use curly brackets to create a dictionary.
# Here we'll use a dictionary to build a program that converts month abbreviations to whole month names

month_Conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print(month_Conversions["Nov"])
print(month_Conversions.get("Nov"))
print(month_Conversions.get("Nob"))
