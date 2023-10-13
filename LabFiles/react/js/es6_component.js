class Workflow extends React.Component {
    constructor(props) {
        super(props);
        this.state = {whatQ: props.initState};
        this.onClick = this.onClick.bind(this);
    }

    onClick() {
        console.log(`onClick():${new Date().getTime()}`);
        this.setState(prevstate => ({
          whatQ: this.getNextQ(prevstate.whatQ)
        }));
    }

    getNextQ(previousQ){
      let nextQ = 'What?';
      switch(previousQ){
          case 'What?': nextQ = 'So What?'; break;
          case 'So What?': nextQ = 'Now What?'; break;
          case 'Now What?': nextQ = 'What?'; break;
          default: nextQ = 'Whadda ...?'; 
      }
      return nextQ;
    }    

    render() {
        console.log(`render():${new Date().getTime()}`);
        return (
          <button onClick={this.onClick}>
            {this.state.whatQ}
          </button>
        );
    }
}

ReactDOM.render(
  <Workflow initState={'What?'}/>,
  document.getElementById('where_to_render')
)