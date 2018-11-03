import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import openSocket from 'socket.io-client';

// const socket = openSocket('http://localhost:8000');

class App extends Component {
  componentDidMount() {
    var socket = openSocket('http://127.0.0.1:5000/');
    socket.on('connect', function() {
        //socket.emit('my_event', {data: 'I\'m connected!'});
        console.log("i'm connected");
    });
    socket.on('my_response', function() {
        console.log("message");
    });

        console.log("editedx");
  }
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Welcome Home.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
}

export default App;
