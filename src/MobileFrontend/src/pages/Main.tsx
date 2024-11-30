import {
    IonContent,
    IonHeader,
    IonPage,
    IonTitle,
    IonToolbar,
    IonItem,
    IonLabel,
    IonButton,
    IonCard,
    IonCardHeader,
    IonCardSubtitle,
    IonCardTitle,
    IonCardContent,
    IonImg, IonAlert
} from '@ionic/react';
import React, {useState} from 'react';
import './Main.css';
import { useHistory } from "react-router-dom";
import Typewriter from "typewriter-effect";


const Main: React.FC = () => {
    const [welcome, setWelcome] = useState(true);
    const history = useHistory();
    const redirectVideo = () => {
        history.push("/videocheck");
    };
    const redirectPhoto = () => {
        history.push("/framecheck");
    };
    return (
        <IonPage>
            <IonContent fullscreen={true}>
                <img src={"assets/vv.jpg"} alt={"matrix"} style={{ filter: "blur(3px)", position: "absolute", height:"100%", width: "100%", zIndex: "1"}}></img>

                <p style={{color:"white", position:"absolute", fontSize: "30px", zIndex: 2, top: "28%", left: "50%", transform: "translate(-50%, -50%)", msTransform: "translate(-50%, -50%)"}}>
                    <Typewriter
                        onInit={(typewriter)=> {
                            typewriter
                                .pauseFor(1000)
                                .changeDelay(100)
                                .typeString("Hello...")
                                .start();
                        }}
                    />
                </p>

                <p style={{marginLeft: "10%", marginRight:"10%", textAlign:"center", color:"white", position:"absolute", fontSize: "18px", zIndex: 2, top: "37%"}}>
                    <Typewriter
                        onInit={(typewriter)=> {
                            typewriter
                                .pauseFor(2000)
                                .changeDelay(50)
                                .typeString("Welcome to the DeepFake Detector")
                                .start()
                        }}
                    />
                    </p>

                <p style={{marginLeft: "10%", marginRight: "10%", textAlign:"center", color:"white", position:"absolute", fontSize: "18px", zIndex: 2, top: "47%"}}>
                    <Typewriter
                        onInit={(typewriter)=> {
                            typewriter
                                .pauseFor(4000)
                                .changeDelay(50)
                                .typeString("Visualize the real/fake probabilities of a video or try out the single frame inference")
                                .start();
                        }}
                    />
                    </p>

                <IonButton onClick={() => redirectVideo()} color={"danger"} style={{ top: "68%", left: "50%", transform: "translate(-50%, -50%)", msTransform: "translate(-50%, -50%)", borderRadius: "3px", position:"absolute", zIndex: "2"}}>
                    Deepfake Video Check
                </IonButton>

                <IonButton onClick={() => redirectPhoto()} color={"danger"} style={{ top: "77%", left: "50%", transform: "translate(-50%, -50%)", msTransform: "translate(-50%, -50%)", borderRadius: "3px", position:"absolute", zIndex: "2"}}>
                    Deepfake Frame Check
                </IonButton>

            </IonContent>
        </IonPage>
    );
};
export default Main;