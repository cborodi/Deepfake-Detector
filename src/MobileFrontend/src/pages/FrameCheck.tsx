import {
    IonContent,
    IonHeader,
    IonPage,
    IonTitle,
    IonToolbar,
    IonItem,
    IonLabel,
    IonButton,
    IonLoading, IonAlert
} from '@ionic/react';
import React, { useRef, useState } from 'react';
import './FrameCheck.css';
import {IonRouteInner} from "@ionic/react-router/dist/types/ReactRouter/IonRouteInner";
import axios from "axios";
interface InternalValues {
    file: any;
}
const FrameCheck: React.FC = () => {
    const [resultdisplayed, setResultdisplayed] = useState(false);
    const [predicted, setPredicted] = useState([]);
    const [probability, setProbability] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [message, setMessage] = useState("");
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
            "http://127.0.0.1:5000/framecheck", formData
        ).then((response)=>{
                if(!response.status){
                    console.log("Failure");
                }
                else{
                    setIsLoading(false);
                    setPredicted(response.data.predicted);
                    setProbability(response.data.probability);
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
                    <IonTitle>Frame Check</IonTitle>
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
                <><br/>
                <IonItem>
                    Frame predicted as {predicted}
                </IonItem><IonItem>
                    Real probability {probability}
                </IonItem></>
                }
            </IonContent>
        </IonPage>
    );
};
export default FrameCheck;