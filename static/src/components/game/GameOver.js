import React from 'react'
import { connect } from 'react-redux'
import { Dialog, DialogTitle, DialogContent, DialogContentText, DialogActions, Button } from '@material-ui/core'
import { setDialogVisibility } from '../../actions/Actions'

const GameOver = ({socket, dialog_visibility, setDialogVisibility, turns}) => {
    const handleClose = () => {
        setDialogVisibility(false)
    };

    const new_game = () => {
        socket.emit('start_game')
        handleClose()
    }

    React.useEffect(() => {
        setDialogVisibility(dialog_visibility)
    }, [dialog_visibility])

    return (
        <Dialog onClose={handleClose} aria-labelledby="simple-dialog-title" open={dialog_visibility}>
            <DialogTitle>{"Game Over."}</DialogTitle>
            <DialogContent>
                <DialogContentText id="alert-dialog-description">
                {turns % 2 === 1 ? "You win!" : "Computer won."}
                </DialogContentText>
            </DialogContent>
            <DialogActions>
              <Button onClick={handleClose} variant="contained">
                Close
              </Button>
              <Button onClick={(new_game)} variant="contained" color="primary" autoFocus>
                New Game
              </Button>
            </DialogActions>
        </Dialog>
    )
}

const mapStateToProps = state => ({
    dialog_visibility: state.game.dialog_visibility,
    turns: state.game.turns,
})
const mapDispatchToProps = dispatch =>({
    setDialogVisibility: (visibility) => dispatch(setDialogVisibility(visibility)),
})
export default connect(mapStateToProps, mapDispatchToProps)(GameOver)
