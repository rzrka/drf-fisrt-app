import React from 'react'

class TodoForm extends React.Component {
    constructor(props) {
        super(props)
        console.log(props.users)
        this.state = {title: '', text: '', user: props.users[0]}
    }

    handleChange(event)
    {
        this.setState(
            {
                [event.target.title]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        this.props.createBook(this.state.title, this.state.text, this.state.user)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="login">title</label>
                    <input type="text" className="form-control" name="title" value={this.state.title} onChange={(event) => this.handleChange(event)} />
                </div>



                <div className="form-group">
                    <label for="users">users</label>

                    <select name="user" className="form-control" onChange={(event) => this.handleChange(event)}>
                        <input type="number" className="form-control" name="user" value={this.state.user} onChange={(event) => this.handleChange(event)} />
                        {this.props.users.map((item)=><option value={item.id}>{item.name}</option>)}
                    </select>
                </div>

                <input type="submit" className="btn btn-primary" value="Save" />
            </form>
       )
    }
}


export default TodoForm