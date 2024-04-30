const express=require('express');
const app=express();
const PORT= process.env.PORT || 5000;

//jsonparsing
app.use(express.json());
//routes
app.use('/api/auth',require('./routes/auth'));

//startserver
app.listen(PORT,()=> console.log('Server running on port ${PORT}'));

