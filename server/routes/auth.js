const express = require('express');
const router = express.Router();
const User = require('../models/User');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

// Signup route
router.post('/signup', async (req, res) => {
  // Extract data from request body
  const { username, email, password } = req.body;

  // Check if user already exists
  const existingUser = await User.findOne({ email });
  if (existingUser) {
    return res.status(400).json({ message: 'User already exists' });
  }

  //hashpassword
  const hashedPassword = await bcrypt.hash(password,10);
  //create new user
  const newUser=new User({
    username,
    email,
    password: hashedPassword,
  })

  try {
    await newUser.save();
    res.status(201).json({message:'User created successfully'});
  } catch (err) {
    res.status(500).json({message:'Server error'})
  }

});

//Login route

router.post('/login',async (req,res)=>{
    const {email,password}=req.body;

    //find user by email
    const user=await User.findOne({email});
    if (!user){
        return res.status(400).json({message:'Invalid credentials'});
    }
    //check password
    const isPasswordVlid = await bcrypt.compare(password,user.password);
    if (!isPasswordVlid){
        return res.status(400).json({message:'Invalid credentials'});

    }
    //generate jwt token
    const token= jwt.sign({userId: user._id},'secret_key',{
        expiresIn: '1h',
    });
    res.status(200).json({token});
});
module.exports=router;