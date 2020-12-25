import './App.css';
import App1 from "./App1";
import Post from "./post";
import axios from 'axios';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
function App() {
  return (
    <Post/>
  );
}

export default App;
