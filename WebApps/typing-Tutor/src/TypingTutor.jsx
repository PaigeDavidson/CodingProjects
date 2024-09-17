export function TypingTutor(props) {
    return(
        <div className="phrase">
            <span className="typedText">{props.typed}</span>
            <span className='underline'>{props.nextChar}</span>
            <span className='untypedText'>{props.untyped}</span>
        </div>
    );
}