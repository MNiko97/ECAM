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
    <div class="cart-box">
        <h1>Your Cart:</h1>
        <div class="user-box">
            <?php 
            echo "<label>Name: ".$_SESSION['name']."</label><br>";
            ?>
        </div>
        <div class="user-box">
            <?php 
            echo "<label>Firstname: ".$_SESSION['firstname']."</label><<br>";
            ?>
        </div>
        <h2>You've chosen the folowing formations:</h2>
        <?php 
        foreach($_SESSION['products'] as $product){
            echo "<div class='user-box'><label>".$product."</label><br></div>";
        }
        ?>
        <h2>For a total price of: <?php echo $_SESSION['total']?>€</h2>
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
        .cart-box {
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
        .cart-box h1 {
            margin: 0 0 50px;
            font-size: 50px;
            padding: 0;
            color: #fff;
            text-align: center;
        }
        .cart-box h2 {
            margin: 0 0 70px;
            font-size: 22px;
            padding: 0;
            color: #fff;
            text-align: center;
        }
        .cart-box .user-box {
            position: relative;
        }
        .cart-box .user-box label {
            position: relative;
            top:-40;
            left: 50;
            padding: 30px 0;
            font-size: 18px;
            color: #fff;
            pointer-events: none;
            transition: .5s;
        }
    </style>
</body>