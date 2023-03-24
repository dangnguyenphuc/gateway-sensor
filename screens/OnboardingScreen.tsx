import React from 'react';
import { View, Text, Button, StyleSheet, Image } from 'react-native';
import { SvgUri } from 'react-native-svg';

import Onboarding from 'react-native-onboarding-swiper';

const OnboardingScreen = ({navigation}: {navigation: any}) => {
    return (
        <Onboarding
            // SkipButtonComponent={Skip}
            onSkip={() => navigation.navigate("Login")}
            onDone={() => navigation.navigate("Login")}
            pages={[
                {
                    backgroundColor: '#fff',
                    image: <Image style={styles.img} source={require('../assets/images/onboarding/onboarding1.png')}/>,
                    title: 'Quản lý từ xa',
                    subtitle: 'Quản lý thiết bị trong nhà đơn giản, tiện lợi bằng điện thoại mọi lúc.',
                    titleStyles: {color: 'blue', fontFamily:'Inter-Bold'},
                    subTitleStyles: {color:'#615858', fontFamily: 'Inter-Regular'}
                },
                {
                    backgroundColor: '#fff',
                    image: <Image style={styles.img} source={require('../assets/images/onboarding/onboarding2.png')}/>,
                    title: 'Siêu tiết kiệm',
                    subtitle: 'Quản lý và đưa ra giải pháp tiêu năng lượng dễ dàng hơn.',
                    titleStyles: {color: 'blue', fontFamily:'Inter-Bold'},
                    subTitleStyles: {color:'#615858', fontFamily: 'Inter-Regular'}
                },
                {
                    backgroundColor: '#fff',
                    image: <Image style={styles.img} source={require('../assets/images/onboarding/onboarding3.png')}/>,
                    title: 'Tương tác tự nhiên',
                    subtitle: 'Ra lệnh trực tiếp cho các thiết bị bằng giọng nói một cách tự nhiên.',
                    titleStyles: {color: 'blue', fontFamily:'Inter-Bold'},
                    subTitleStyles: {color:'#615858', fontFamily: 'Inter-Regular'}
                },               
            ]}
        />
    );
};

export default OnboardingScreen;

const styles = StyleSheet.create({
    container: {
        flex: 1, 
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: 'blue'
    },
    img: {
        width: 300,
        height: 300,
        justifyContent:'center',
        position: 'absolute',
        top: -250,
        // borderWidth: 5,

        // borderColor: 'red',
    }
});