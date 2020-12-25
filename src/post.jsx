import  React,{useState,useEffect} from "react";
import axios from 'axios';
import Csrf from "./Csrf";
// axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
// axios.defaults.xsrfCookieName = "csrftoken";
// axios.defaults.withCredentials = true;
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
const Post=()=>{
    useEffect(()=>{
        
    })
const [data,setData]=useState({
    "username":"",
    "email":"",
    "password":"",
})

// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }
// const csrftoken = getCookie('csrftoken');

const inputEvent=(event)=>{
   const {name,value}=event.target;
   setData((prevValue)=>{
        return{...prevValue,
            [name]:value,
        };
   })
}

const handleSubmit=(e)=>{
    e.preventDefault()
    axios.post('http://127.0.0.1:8000/user/register/',data,
    // {
    //     "username":data.username,
    //     "email":data.email,
    //     "phone":data.phone,
    //     "name":data.name,
    //     "password":data.password
    // },

    // {
    //     headers:{
        
    //         xsrfHeaderName : "X-CSRFTOKEN",
    //         xsrfCookieName : "csrftoken",
    //         'X-Requested-With': 'XMLHttpRequest',
    //     }

    // },
    )
          .then(function (response) {
              console.log(response)
          })
          .catch(function (error) {
              console.log(error)
          })
}
return(
    <>
    <form action="" method="post" onSubmit={handleSubmit}>
        {/* /<Csrf/>* */}
    <input type="text" placeholder="username" name="username" onChange={inputEvent} value={data.username} required/>
    <br/><br/>
    <input type="email" placeholder="Email" name="email" onChange={inputEvent} value={data.email} required/>
    <br/><br/>
    <input type="text" placeholder="password" name="password" onChange={inputEvent} value={data.password} required/>
    <br/><br/>

    <button type="submit" > Submit </button>
    </form>
        
    </>
)



}
export default Post;