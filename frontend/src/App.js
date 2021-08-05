import React from "react";
import axios from 'axios';

import UsersList from "./components/users";
import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      'users': [],
    }
  }
  componentDidMount() {
    axios.get('http://127.0.0.1:8000/users')
    .then(response => {
      const users = response.data
      this.setState(
        {
          'users': users,
        }
      )
    }).catch(error => console.log(error))
  }

  render() {
    return (
      <div>
        <UsersList items={this.state.users} />
      </div>
    )
  }
}

export default App

