import React from 'react'
import { connect } from 'react-redux'
import Button from '@material-ui/core/Button';

class Landing extends React.Component {
    constructor(props){
        super(props);
    }
    render(){
        return (
            <div>
                  {this.props.page}
            </div>
        )

    }
}

const mapStateToProps = state => ({
    page: state.page.page
})
export default connect(
  mapStateToProps,
  null,
)(Landing)
