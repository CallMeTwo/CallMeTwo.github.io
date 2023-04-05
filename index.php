<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <title> PHP </title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/styles.css') }}" />
</head>

<body>
    <div class="main">
        <form action= <?php echo $_SERVER['PHP_SELF']; ?> method="post">
            <p>
                Tcb <input type="text" name="mb" />
            </p>
            <p>
                GA : <input type="number" id="ga" maxlength="2" min="35" max="50" name="ga" />
            </p>
            <p>
                Age <input type="text" name="age" />
            </p>
            <p>
                Birth <input type="datetime-local" name="time1" />
            </p>
            <p>
                Today <input type="datetime-local" name="time2" />
            </p>
            <span> Risk </span>
            <input type="radio" name="risk" id="low" value="low" />
            <label for="html"> Low </label>
            <input type="radio" name="risk" id="high" value="high" />
            <label for="css"> High </label>
            <p>
                <input type="submit" name="submit" value="Submit Form" /><br />
            </p>
        </form>
    </div>

    <div class="confirm">
        <p>
            GA = <span class="resulttext"> </span>
        </p>
        <p>
            Age = <span class="resulttext"> </span>
        </p>
        <p>
            Risk = <span class="resulttext"> </span>
        </p>
        <p>
            Tcb = 
            <?php
            if(isset($_POST['submit']))
            {
                $name = $_POST['mb'];
                echo " $name ";
            }
            ?>
        </p>
    </div>
    <div class="result">
        <p>Photo = </p>
        <p>Tranfusion = </p>
    </div>

    <?php
    echo('hello');
    ?>
</body>
</html>