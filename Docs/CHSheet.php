<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Character building</title>
</head>
<body>
<form action="create_sheet.html" method="post" >
    All fields with a: * are mandatory. <br><br>
    *Player name: <input required type="text" name="PlayerName" placeholder="Player name" value="<?php echo isset($_POST['PlayerName']) ? $_POST['myField1'] : '' ?>" ><br>
    *Character name: <input required type="text" name="CharacterName" placeholder="Character name"><br>
    *Eye color: <input required type="text" name="EyeColor" placeholder="Eye color"><br>
    *Hair color: <input required type="text" name="HairColor" placeholder="Hair color"><br>
    *Age: <input required type="text" name="Age" placeholder="Age"><br>
    *Race: <input required type="text" name="Race" placeholder="Race"><br>
    <br>
    *Gender: <br>
    <input type="radio" name="Gender" value="male" checked> Male <br>
    <input type="radio" name="Gender" value="female"> Female <br><br>
    *Allignement: <br>
    <input type="radio" name="Allignment" value="Lawfull good" checked> Lawfull good <br>
    <input type="radio" name="Allignment" value="Lawfull neutral"> Lawfull neutral <br>
    <input type="radio" name="Allignment" value="Lawfull evil"> Lawfull evil <br>
    <input type="radio" name="Allignment" value="Neutral good" checked> Neutral good <br>
    <input type="radio" name="Allignment" value="Neutral" checked> Neutral <br>
    <input type="radio" name="Allignment" value="Neutral evil"> Neutral evil <br>
    <input type="radio" name="Allignment" value="Chaotic good" > Chaotic good <br>
    <input type="radio" name="Allignment" value="Chaotic neutral"> Chaotic neutral <br>
    <input type="radio" name="Allignment" value="Chaotic evil"> Chaotic evil <br>
    <br>
    Tatoos /scars /piercings /marks: <br><textarea name="Marks" style="width: 300px; height: 100px;"  placeholder="Tatoos, scars, piercings, etc."></textarea><br>
    <br>
    General description: <br><textarea name="description" style="width: 300px; height: 100px;"  placeholder="General description."></textarea><br>
    <br>








    <input type="submit" value="Submit">
</form>


</body>
</html>