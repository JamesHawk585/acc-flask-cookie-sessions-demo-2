import { useEffect } from "react"
import './App.css';

function App() {
  /*
  - Use useEffect to:
    - send a get request to '/cookies'
    - parse resp as json and console.log resp
    - console.log document.cookie
      - Note the cookies that are marked as HTTP only
  */
 
  return (
    <div className="App">
      <h1>httpOnly demo</h1>
    </div>
  );
}

export default App;
