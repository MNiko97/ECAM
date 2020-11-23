<?php
session_start();
$selected_products = array();
$total = 0;
$products = array(
            array('id'=> 0, 'name' => 'PHP', 'price' => 250, 'description'=>'PHP 250€'), 
            array('id'=> 1, 'name' => 'XML', 'price' => 350, 'description'=>'XML 350€'), 
            array('id'=> 2, 'name' => 'JAVA', 'price' => 450, 'description'=>'JAVA 450€'), 
            array('id'=> 3, 'name' => 'C++', 'price' => 550, 'description'=>'C++ 550€'));
?>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Programming Formations</title>
</head>
<body>
    <div class="product-box">
        <h2>Select Formations</h2>
        <form method="POST">
        <?php 
        // generate checkbox with the products array
        foreach($products as $formation){
            echo "<div class='user-box'><input type='checkbox' name='formation[]' value='".$formation['id']."'>";
            echo "<label>".$formation['description']."</label></div>";
        }
        echo "<br>";
        ?>
        <input type="submit" name="next_btn" id="next_btn" value="Next"> 
        </form> 
        <form method="POST">
            <input type="submit" name="cancel_btn" id="cancel_btn" value="Cancel">  
            <input type="submit" name="back_btn" id="back_btn" value="Back" >
        </form>
        <form method="POST">
            <input type="submit" name="view_session_btn" id="view_btn" value="View Session">
        </form>
        <?php
        if(isset($_POST['next_btn'])){
            if (isset($_POST['formation']) && !empty($_POST['formation'])){
                foreach($_POST['formation'] as $value){
                    array_push($selected_products, $products[$value]['name']); 
                    $total += $products[$value]['price'];
                } 
                // add session variables for cart.php
                $_SESSION['total'] = $total;
                $_SESSION['products'] = $selected_products;
                header('Location: cart.php');
            }
            else{
                echo "<div class='user-box'>You dit not choose a formation.</div>";
            }
        }
        if(isset($_POST['cancel_btn'])){
            session_destroy();
            header('Location: index.php');
        }
        if(isset($_POST['back_btn'])){
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
        .product-box {
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
        .product-box h2 {
            margin: 0 0 30px;
            padding: 0;
            color: #fff;
            text-align: center;
        }
        .product-box .user-box {
            position: relative;
            color: white;
        }
        .product-box .user-box input {
            position: relative;
            left: 35px;
            width: 50%;
            padding: 10px 0;
            color: #fff;
            margin-bottom: 30px;
        }
        .product-box .user-box label {
            position: absolute;
            top:-10;
            left: 140;
            padding: 10px 0;
            font-size: 16px;
            color: #fff;
            pointer-events: none;
            transition: .5s;
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
            left: 230px;
        }
        #back_btn{
            position: relative;
            left: 130px;
        }
        #cancel_btn{
            position: relative;
            left: -5px;
        }
        #view_btn{
            position: relative;
            left: -6px;
        }
    </style>
</body>