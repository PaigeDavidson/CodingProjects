export function Keyboard(props){

    let rowOne = [
        {id:1, key:"`"}, {id:2, key:"1"}, {id:3, key:"2"}, {id:4, key:"3"}, {id:5, key:"4"},
        {id:6, key:"5"}, {id:7, key:"6"}, {id:8, key:"7"}, {id:9, key:"8"},{id:10, key:"9"},
        {id:11, key:"0"}, {id:12, key:"-"}, {id:13, key:"="}
    ]
    
    let rowTwo = [
        {id:1, key:"q"}, {id:2, key:"w"}, {id:3, key:"e"}, {id:4, key:"r"}, {id:5, key:"t"},
        {id:6, key:"y"}, {id:7, key:"u"}, {id:8, key:"i"}, {id:9, key:"o"},{id:10, key:"p"},
        {id:11, key:"["}, {id:12, key:"]"},{id:13, key:"\\"}
    ]
    let rowThree = [
        {id:1, key:"a"}, {id:2, key:"s"}, {id:3, key:"d"}, {id:4, key:"f"}, {id:5, key:"g"},
        {id:6, key:"h"}, {id:7, key:"j"}, {id:8, key:"k"}, {id:9, key:"l"}, {id:10, key:";"},
        {id:11, key:"'"},
    ]
    let rowFour = [
        {id:1, key:"Shift"}, {id:2, key:"z"}, {id:3, key:"x"},{id:4, key:"c"},
        {id:5, key:"v"}, {id:6, key:"b"}, {id:7, key:"n"}, {id:8, key:"m"},
        {id:9, key:","}, {id:10, key:"."}, {id:11, key:"/"}, {id:12, key:"Shift"},
    ]
    let rowFive = [
        {id:1, key:" "},
    ]

    if(props.keys.includes("Shift")){
        //change all the keys to the shift keys
        rowOne = [
            {id:1, key:"~"}, {id:2, key:"!"}, {id:3, key:"@"}, {id:4, key:"#"},
            {id:5, key:"$"}, {id:6, key:"%"}, {id:7, key:"^"}, {id:8, key:"&"}, 
            {id:9, key:"*"}, {id:10, key:"("}, {id:11, key:")"}, {id:12, key:"_"},
            {id:13, key:"+"}
        ]
        rowTwo = [
            {id:1, key:"Q"}, {id:2, key:"W"}, {id:3, key:"E"}, {id:4, key:"R"}, 
            {id:5, key:"T"}, {id:6, key:"Y"}, {id:7, key:"U"}, {id:8, key:"I"},
            {id:9, key:"O"}, {id:10, key:"P"}, {id:11, key:"{"}, {id:12, key:"}"},
            {id:13, key:"|"}
        ]
        rowThree = [
            {id:1, key:"A"}, {id:2, key:"S"}, {id:3, key:"D"},{id:4, key:"F"},{id:5, key:"G"},
            {id:6, key:"H"},{id:7, key:"J"},{id:8, key:"K"},{id:9, key:"L"},{id:10, key:":"},
            {id:11, key:'"'},
        ]
        rowFour = [
            {id:1, key:"Shift"}, {id:2, key:"Z"}, {id:3, key:"X"},{id:4, key:"C"},
            {id:5, key:"V"}, {id:6, key:"B"}, {id:7, key:"N"}, {id:8, key:"M"},
            {id:9, key:"<"}, {id:10, key:">"}, {id:11, key:"?"},{id:12, key:"Shift"}
        ]
    }
    return (
        <div className="keyboard">
            <div className='keyboard-row'>
                {
                    rowOne.map((char) => {
                        let className = "keyboard-key"
                        if(props.keys.includes(char.key)){
                            className = "keyboard-key active"
                        }
                        if(props.nextChar === char.key){
                            className = "keyboard-key highlighted"
                        }
                        return(
                            <div key={char.id} className={className}>
                                <div>{char.key}</div>
                            </div>
                        )
                    })
                }
            </div>
            <div className='keyboard-row'>
                        {
                            rowTwo.map((char) => {
                                let className = "keyboard-key"
                                if(props.keys.includes(char.key)){
                                    className = "keyboard-key active"
                                }
                                if(props.nextChar === char.key){
                                    className = "keyboard-key highlighted"
                                }
                                return(
                                    <div key={char.id} className={className}>
                                        <div>{char.key}</div>
                                    </div>
                                )
                            })
                        }
            </div>
            <div className='keyboard-row'>
                        {
                            rowThree.map((char) => {
                                let className = "keyboard-key"
                                if(props.keys.includes(char.key)){
                                    className = "keyboard-key active"
                                }
                                if(props.nextChar === char.key){
                                    className = "keyboard-key highlighted"
                                }
                                return(
                                    <div key={char.id} className={className}>
                                        <div>{char.key}</div>
                                    </div>
                                )
                            })
                        }
            </div>
            <div className='keyboard-row'>
                        {
                            rowFour.map((char) => {
                                let className = "keyboard-key"
                                if(props.keys.includes(char.key)){
                                    className = "keyboard-key active"
                                }
                                if(props.nextChar === char.key){
                                    className = "keyboard-key highlighted"
                                }
                                if(char.id === 1 || char.id === 12){
                                    className = "keyboard-key shift"

                                    if(props.keys.includes(char.key)){
                                        className = "keyboard-key shift active"
                                    }
                                }
                                if((char.id === 1 || char.id === 12) && props.isShift){
                                    className = "keyboard-key shift highlighted"
                                    if(props.keys.includes(char.key)){
                                        className = "keyboard-key shift active"
                                    }
                                }
                                return(
                                    <div key={char.id} className={className}>
                                        <div>{char.key}</div>
                                    </div>
                                )
                            })
                        }
            </div>
            <div className='keyboard-row'>
                        {
                            rowFive.map((char) => {
                                let className = "keyboard-key space-bar"
                                if(props.keys.includes(char.key)){
                                    className = "keyboard-key space-bar active"
                                }
                                if(props.nextChar == char.key){
                                    className = "keyboard-key space-bar highlighted"
                                }
                                return(
                                    <div key={char.id} className={className}>
                                        <div>{char.key}</div>
                                    </div>
                                )
                            })
                        }
            </div>
        </div>
    );
}