import React from "react";
import axios from 'axios';
import Cookies from 'universal-cookie';
import {HashRouter, Route, Link, Redirect, Switch, BrowserRouter} from 'react-router-dom'

import UsersList from "./components/users";
import ProjectsList from "./components/Projects";
import TodoList from "./components/Todo";
import LoginForm from './components/Auth'
import './App.css';

class App extends React.Component {

  set_token(token) {
    const cookies = new Cookies()
    cookies.set('token', token)
    this.setState({'token': token}, ()=>this.load_data())

  }

  get_headers() {
    let headers = {
      'Content-Type': 'application/json'
    }
    if (this.is_authenticated())
    {
        headers['Authorization'] = 'Token ' + this.state.token
    }
    return headers
  }

  is_authenticated() {
    return this.state.token != ''
  }

  logout() {
    this.set_token('')
  }

  get_token_from_storage() {
    const cookies = new Cookies()
    const token = cookies.get('token')
    this.setState({'token': token}, ()=>this.load_data())
    console.log(cookies)
  }

  get_token(username, password) {
    axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
    .then(response => {
        this.set_token(response.data['token'])
    }).catch(error => alert('неверный логин и пароль'))
  }

  load_data() {

  const headers = this.get_headers()

  axios.get('http://127.0.0.1:8000/projects', {headers})
    .then(response => {
      this.setState(
        {
          'projects': response.data,
        }
      )
    }).catch(error => console.log(error))


  axios.get('http://127.0.0.1:8000/users', {headers})
    .then(response => {
      this.setState(
        {
          'users': response.data,
        }
      )
    }).catch(error => console.log(error))


  axios.get('http://127.0.0.1:8000/todo', {headers})
    .then(response => {
      this.setState(
        {
          'todo': response.data,
        }
      )
    }).catch(error => console.log(error))

  }
  constructor(props) {
    super(props);
    this.state = {
      'users': [],
      'projects': [],
      'todo': [],
      'token': ''
    }
  }
  componentDidMount() {
  this.get_token_from_storage()
  }

  render() {
    return (
      <div className="App">
        <BrowserRouter>
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
              <li>
                {this.is_authenticated() ? <button onClick={() => this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
              </li>
            </ul>
          </nav>
          <Switch>
            <Route exact path='/users' component={() => <UsersList items={this.state.users} />} />
            <Route exact path='/projects' component={() => <ProjectsList items={this.state.projects} />} />
            <Route exact path='/todo' component={() => <TodoList items={this.state.todo} />} />
            <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
            <Route path='/user/:id'>
              <ProjectsList items={this.state.projects} />
            </Route>
            <Redirect from='/users' to='/' />
          </Switch>  
        </BrowserRouter>
      </div>
    )
  }
}

export default App
