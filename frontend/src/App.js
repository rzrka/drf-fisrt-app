import React from "react";
import axios from 'axios';
import {HashRouter, Route, Link} from 'react-router-dom'

import UsersList from "./components/users";
import ProjectsList from "./components/Projects";
import TodoList from "./components/Todo";
import './App.css';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      'users': [],
      'projects': [],
      'todo': [],
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
    axios.get('http://127.0.0.1:8000/projects')
    .then(response => {
      const projects = response.data
      this.setState(
        {
          'projects': projects,
        }
      )
    }).catch(error => console.log(error))
    axios.get('http://127.0.0.1:8000/todo')
    .then(response => {
      const todo = response.data
      this.setState(
        {
          'todo': todo,
        }
      )
    }).catch(error => console.log(error))
  }

  render() {
    return (
      <div className="App">
        <HashRouter>
          <nav>
            <ul>
              <li>
                <Link to='/users'>Users</Link>
              </li>
              <li>
                <Link to='/projects'>Projects</Link>
              </li>
              <li>
                <Link to='/todo'>Todo</Link>
              </li>
            </ul>
          </nav>
          <Route exact path='/users' component={() => <UsersList items={this.state.users} />} />
          <Route exact path='/projects' component={() => <ProjectsList items={this.state.projects} />} />
          <Route exact path='/todo' component={() => <TodoList items={this.state.todo} />} />
        </HashRouter>
      </div>
    )
  }
}

export default App

