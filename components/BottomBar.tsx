import * as React from 'react';
import { View, Text, StyleSheet,Button, Image, ScrollView, Switch } from 'react-native';
import Icon3 from 'react-native-vector-icons/FontAwesome';

const BottomBar = () => {
    return (
        <View style={styles.footer}>
            <View style={styles.leftFooterContainer}>
                <Image style={styles.leftFooterButton} source={require('../assets/images/home/left_footer.png')}/>
            </View>

            <View style={styles.middleFooterContainer}>
                <View style={styles.circleContainer}>
                    <Icon3 style={styles.middleIconFooterButton} name="microphone" size={50} color="black"/>
                </View>
            </View>

            <View style={styles.rightFooterContainer}>
                <Image style={styles.rightFooterButton} source={require('../assets/images/home/right_footer.png')}/>
                <Icon3 style={styles.rightIconFooterButton} name="user-o" size={50} color="white"/>
            </View>
        </View>
)};


export default BottomBar;

const styles = StyleSheet.create({
    // footer
    footer: {
        flex: 1.25,
        flexDirection: 'row',
        // backgroundColor: 'blue'
        backgroundColor: '#EFF1F5',

    },
    rightFooterContainer: {
        flex: 1,
    },
    middleFooterContainer: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
    },
    leftFooterContainer: {
        flex: 1
    },
    leftFooterButton: {
        flex: 1,
        justifyContent: 'flex-start',
        width: '100%',
        // height: 'undefined',
    },
    rightFooterButton: {
        flex: 1,
        justifyContent: 'flex-end',
        width: '100%',
        // position: 'relative'
    },
    circleContainer: {
        position: 'absolute',
        justifyContent: 'center',
        alignItems: 'center',
        width: 75,
        height: 75,
        borderRadius: 100 / 2,
        backgroundColor: 'red',
    },
    middleIconFooterButton: {
        alignItems: 'center',
        // backgroundColor: 'blue',
        
    },
    rightIconFooterButton: {
        position: 'absolute',
        alignItems: 'flex-end',
        top: 25,
        left: 82,

    }
});