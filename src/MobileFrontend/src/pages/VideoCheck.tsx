import {
    IonContent,
    IonHeader,
    IonPage,
    IonTitle,
    IonToolbar,
    IonItem,
    IonLabel,
    IonButton,
    IonLoading,
    IonAlert
} from '@ionic/react';
import React, {useRef, useState} from 'react';
import './VideoCheck.css';
import axios from "axios";
import {Simulate} from "react-dom/test-utils";
interface InternalValues {
    file: any;
}
const VideoCheck: React.FC = () => {
    const [resultdisplayed, setResultdisplayed] = useState(false);
    const [rprobability, setRprobability] = useState([]);
    const [fprobability, setFprobability] = useState([]);
    const [framenumber, setFramenumber] = useState([]);
    const [faceframes, setFaceframes] = useState([]);
    const [message, setMessage] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const [isError, setIsError] = useState(false);
    const values =
        useRef <
        InternalValues >
        ({
            file: false,
        });
    const onFileChange = (fileChangeEvent: any) => {
        values.current.file = fileChangeEvent.target.files[0];
    };
    const submitForm = async () => {
        if (!values.current.file) {
            return false;
        }
        let formData = new FormData();
        formData.append('file', values.current.file, values.current.file.name);
        setIsLoading(true);
        const api = axios.post(
            "http://127.0.0.1:5000/videocheck", formData
        ).then((response)=>{
                if(!response.status){
                    console.log("Failure");
                }
                else{
                    setIsLoading(false);
                    setRprobability(response.data.realProbability);
                    setFprobability(response.data.fakeProbability);
                    setFramenumber(response.data.totalFrames);
                    setFaceframes(response.data.faceFrames);
                    setResultdisplayed(true);
                    console.log(response);
                }
            }
        ).catch((error) => {
                setIsLoading(false);
                setMessage(error.response.data.message);
                setIsError(true);
                console.log(error);
            }
        )
    };
    return (
        <IonPage>
            <IonHeader>
                <IonToolbar color={"tertiary"} style={{ witdh: "100px" }}>
                    <IonTitle>Video Check</IonTitle>
                </IonToolbar>
            </IonHeader>
            <IonContent>
                <IonLoading isOpen={isLoading} message="This might take a moment..."/>

                <br/><br/>
                <IonItem>
                    <input type="file" onChange={(ev) => onFileChange(ev)}></input>
                </IonItem>
                <IonButton style={{ margin: "10%", display: "block" }} color="warning" expand="full" onClick={() => submitForm()}>
                    Upload
                </IonButton>

                <IonAlert
                    isOpen={isError}
                    onDidDismiss={() => setIsError(false)}
                    cssClass="my-custom-class"
                    header={"Error!"}
                    message={message}
                    buttons={["Dismiss"]}
                />

                { resultdisplayed == true &&
                <>
                    <IonItem>
                        Real probability {rprobability}
                    </IonItem>
                    <IonItem>
                        Fake probability {fprobability}
                    </IonItem>
                    <IonItem>
                        Number of frames {framenumber}
                    </IonItem>
                    <IonItem>
                        Face frames {faceframes}
                    </IonItem>
                    <IonItem>
                        Estimation: { rprobability < fprobability ? <p style={{ color: "red"}}>Fake</p> : <p style={{ color: "green"}}>Real</p>}
                    </IonItem>
                </>
                }
            </IonContent>
        </IonPage>
    );
};
export default VideoCheck;