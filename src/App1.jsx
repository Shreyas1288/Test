import React from "react";
import { useState, useEffect } from 'react';
import axios from 'axios';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
const App1=()=>{
  const [data1,setData]=useState([]);
  useEffect( () => {
    const fetchData= async ()=>{
    const result = await axios(
      'http://127.0.0.1:8000/api/proj/',
    );
    // console.log(result);
    // console.log(result.data);
    console.log(result.data[0].username);
    setData(result.data);
    //  console.log(data1);
  //  console.log(data);
    }
    fetchData();
  },[]);
  return (
    <ul>
      {data1.map(item => (
        <li key={item.username}>
          `my username {item.username} and my email is {item.email} and my phone {item.phone}`
        </li>
      ))}
    </ul>

  );
}


  export default App1;