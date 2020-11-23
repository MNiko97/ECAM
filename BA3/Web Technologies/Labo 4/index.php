<?php
session_start();
?>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Programming Formations</title>
</head>
<body>
    <div class="login-box">
        <h2>Log In</h2>
        <form method="POST">
            <div class="user-box">
                <input type="text" name="name" value="<?php if(isset($_SESSION['name'])){echo $_SESSION['name'];}else echo""?>" required>
                <label>Name</label>
            </div>
            <div class="user-box">
                <input type="text" name="firstname" value="<?php if(isset($_SESSION['firstname'])){echo $_SESSION['firstname'];}else echo ""?>" required>
                <label>Firstname</label>  
            </div>
            <input type="submit"  name="cancel_btn" id="cancel_btn" value="CANCEL">
            <input type="submit" name="next_btn" id="next_btn" value="NEXT">
        </form>
        <form method="POST">
            <input type="submit" name="view_session_btn" id="view_btn" value="View Session">    
        </form>
    <?php
    if(isset($_POST['next_btn'])){
        if(isset($_POST['name']) && $_POST['name'] != " "){
            $_SESSION['name'] = htmlspecialchars($_POST['name']);
        }
        if(isset($_POST['firstname']) && $_POST['firstname'] != " "){
            $_SESSION['firstname'] = htmlspecialchars($_POST['firstname']);
        }
        if(isset($_SESSION['name']) && isset($_SESSION['firstname'])){
            unset($_SESSION['err_msg']);
            header('Location: products.php');
        }
        else{
            $_SESSION['err_msg'] = "bad login";
        }
    }
    if(isset($_POST['cancel_btn'])){
        session_destroy();
        header('Location: index.php');
    }
    if(isset($_POST['view_session_btn'])){
        echo "<div class='user-box'><pre>".print_r($_SESSION, TRUE)."</pre></div>";
    }
    ?>
    </div>
    <style>
        html {
	        height: 100%;
        }
        body {
            margin:0;
            padding:0;
            font-family: sans-serif;
            background: linear-gradient(#141e30, #243b55);
        }
        .login-box {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 400px;
            padding: 40px;
            transform: translate(-50%, -50%);
            background: rgba(0,0,0,.5);
            box-sizing: border-box;
            box-shadow: 0 15px 25px rgba(0,0,0,.6);
            border-radius: 10px;
        }
        .login-box h2 {
            margin: 0 0 30px;
            padding: 0;
            font-size: 50;
            color: #fff;
            text-align: center;
        }
        .login-box .user-box {
            position: relative;
            color: white;
        }
        .login-box .user-box input {
            width: 100%;
            padding: 10px 0;
            font-size: 16px;
            color: #fff;
            margin-bottom: 30px;
            border: none;
            border-bottom: 1px solid #fff;
            outline: none;
            background: transparent;
        }
        .login-box .user-box label {
            position: absolute;
            top:0;
            left: 0;
            padding: 10px 0;
            font-size: 16px;
            color: #fff;
            pointer-events: none;
            transition: .5s;
        }
        .login-box .user-box input:focus ~ label,
        .login-box .user-box input:valid ~ label {
            top: -20px;
            left: 0;
            color: #03e9f4;
            font-size: 12px;
        }
        input[type=submit]{
            display: inline-block;
            margin: 0 auto;
            line-height: 28pt;
            padding: 0 20px;
            background: linear-gradient(#141e30, #243b55);
            color: white;
            letter-spacing: 2px;
            transition: 0.2s all ease-in-out;
            outline: none;
            border: 1px solid black;
        }
        #next_btn {
            position: relative;
            left: 125px;
        }
        #cancel_btn{
            position: relative;
            left: -5px;
        }
        #view_btn{
            position: relative;
            left: -5px;
        }
    </style>
</body>