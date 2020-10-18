import React from 'react'
import { connect } from 'react-redux'
import { TextField, Button } from '@material-ui/core'
import { login } from '../../actions/Actions'

const Login = ({login}) => {
    const [username, setUsername] = React.useState('')

    const onSubmitUsername = (e) => {
        e.preventDefault()
        login(username)
    }

    return (
        <div>
            <form>
                <TextField id='standard-basic' label='username' onChange={e => setUsername(e.target.value)}/>
                <Button variant='outlined' type='submit' onClick={onSubmitUsername}>Submit</Button>
            </form>
        </div>
    )
}

const mapStateToProps = state => ({
})
const mapDispatchToProps = dispatch =>({
    login: (username) => dispatch(login(username))
})
export default connect(
  null,
  mapDispatchToProps,
)(Login)
