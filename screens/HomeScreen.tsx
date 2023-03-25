import * as React from 'react';
import { View, Text, StyleSheet,Button, Image, ScrollView, Switch } from 'react-native';
import Icon from 'react-native-vector-icons/MaterialCommunityIcons';
import Icon1 from 'react-native-vector-icons/Ionicons';
import Icon3 from 'react-native-vector-icons/FontAwesome';
import Icon2 from 'react-native-vector-icons/Feather';

const HomeScreen = ({navigation}: {navigation: any}) =>{
    const [isEnabled, setIsEnabled] = React.useState(false);
    const toggleSwitch = () => setIsEnabled((previousState: Boolean) => !previousState);
    return (
        <View style={styles.container}>
            <View style={styles.subContainer}>

                {/* Header */}
                <View style={styles.headerWrapper}>
                    <View style={styles.headerTitle}>
                        <Text style={{fontSize: 30, fontFamily: 'Inter-Bold', }}>Xin chào Natasha!</Text>
                        <Text style={{position: 'absolute', fontSize: 60, fontFamily: 'Inter-Bold', opacity: 0.1}}>HOME</Text>
                    </View>
                    <View style={styles.headerNotification}>
                        <Icon1 name="notifications-outline" size={50} color="blue"/>
                    </View>
                </View>

                {/* Weather widget */}
                <View style={styles.weatherWidget}>
                    <Image source={require('../assets/images/home/weather_widget.png')}/>
                    <View style={styles.weatherInfor}>
                        <View style={styles.locationInfor}>
                            <Text style={styles.locationTitle}>Vị trí nhà bạn</Text>
                            <Text style={styles.location}>Thủ Đức, Tp.Hồ Chí Minh</Text>
                            <View style={styles.weatherStateContainer}>
                                <Icon2  name="cloud" size={30} color="white"/>
                                <Text style={styles.weatherState}>Partly Cloudy</Text>
                            </View>
                        </View>
                        <View style={styles.weatherTemp}>
                            <View style= {styles.tempContainer}>
                                <Text style={styles.tempInfor}>32</Text>
                                <Text style={{color: 'white', fontSize: 24, fontFamily: 'Inter-Light',}}>o</Text>
                                <Text style={styles.tempInfor}>C</Text>
                            </View>
                            <Text style={styles.humidity}>Độ ẩm: 69%</Text>
                        </View>
                    </View>
                </View>
                <View style={styles.elementDetail}>
                    <View style={styles.roomDetail}>
                        <ScrollView horizontal={true}>
                            <View style={styles.roomCell}><Text>Phòng khách</Text></View>
                            <View style={styles.roomCell}><Text>Phòng ngủ</Text></View>
                            <View style={styles.roomCell}><Text>Nhà bếp</Text></View>
                            <View style={styles.roomCell}><Text>Nhà vệ sinh</Text></View>
                            <View style={styles.roomCell}><Text>Garage</Text></View>
                        </ScrollView>

                    </View>
                    <ScrollView style={styles.listDetail}>
                        <View style={styles.listDetailRow}>
                            <View style={styles.box}>
                                <Icon style={styles.iconBox} name="lightbulb-on-outline" size={50} color="white"/>
                                <Text style={styles.titleBox}> Đèn</Text>
                                <View style={styles.stateBox}>
                                    <Text style={styles.stateTextBox}> Bật</Text>
                                    <Switch         
                                        trackColor={{false: '#767577', true: '#81b0ff'}}
                                        thumbColor={isEnabled ? '#f5dd4b' : '#f4f3f4'}
                                        ios_backgroundColor="#3e3e3e"
                                        onValueChange={toggleSwitch}
                                        value={isEnabled}
                                        style={styles.toggleInBox}
                                    />
                                </View>
                            </View>
                            <View style={styles.box}>
                                <Icon style={styles.iconBox} name="lightbulb-on-outline" size={50} color="white"/>
                                <Text style={styles.titleBox}> Đèn</Text>
                                <View style={styles.stateBox}>
                                    <Text style={styles.stateTextBox}> Bật</Text>
                                    <Switch         
                                        trackColor={{false: '#767577', true: '#81b0ff'}}
                                        thumbColor={isEnabled ? '#f5dd4b' : '#f4f3f4'}
                                        ios_backgroundColor="#3e3e3e"
                                        onValueChange={toggleSwitch}
                                        value={isEnabled}
                                        style={styles.toggleInBox}
                                    />
                                </View>
                            </View>
                        </View>
                        <View style={styles.listDetailRow}>
                            <View style={styles.box}>
                                <Icon style={styles.iconBox} name="lightbulb-on-outline" size={50} color="white"/>
                                <Text style={styles.titleBox}> Đèn</Text>
                                <View style={styles.stateBox}>
                                    <Text style={styles.stateTextBox}> Bật</Text>
                                    <Switch         
                                        trackColor={{false: '#767577', true: '#81b0ff'}}
                                        thumbColor={isEnabled ? '#f5dd4b' : '#f4f3f4'}
                                        ios_backgroundColor="#3e3e3e"
                                        onValueChange={toggleSwitch}
                                        value={isEnabled}
                                        style={styles.toggleInBox}
                                    />
                                </View>
                            </View>
                            <View style={styles.box}>
                                <Icon style={styles.iconBox} name="lightbulb-on-outline" size={50} color="white"/>
                                <Text style={styles.titleBox}> Đèn</Text>
                                <View style={styles.stateBox}>
                                    <Text style={styles.stateTextBox}> Bật</Text>
                                    <Switch         
                                        trackColor={{false: '#767577', true: '#81b0ff'}}
                                        thumbColor={isEnabled ? '#f5dd4b' : '#f4f3f4'}
                                        ios_backgroundColor="#3e3e3e"
                                        onValueChange={toggleSwitch}
                                        value={isEnabled}
                                        style={styles.toggleInBox}
                                    />
                                </View>
                            </View>
                        </View>
                        <View style={styles.listDetailRow}>
                            <View style={styles.box}>
                                <Icon style={styles.iconBox} name="lightbulb-on-outline" size={50} color="white"/>
                                <Text style={styles.titleBox}> Đèn</Text>
                                <View style={styles.stateBox}>
                                    <Text style={styles.stateTextBox}> Bật</Text>
                                    <Switch         
                                        trackColor={{false: '#767577', true: '#81b0ff'}}
                                        thumbColor={isEnabled ? '#f5dd4b' : '#f4f3f4'}
                                        ios_backgroundColor="#3e3e3e"
                                        onValueChange={toggleSwitch}
                                        value={isEnabled}
                                        style={styles.toggleInBox}
                                    />
                                </View>
                            </View>
                            <View style={styles.box}>
                                <Icon style={styles.iconBox} name="lightbulb-on-outline" size={50} color="white"/>
                                <Text style={styles.titleBox}> Đèn</Text>
                                <View style={styles.stateBox}>
                                    <Text style={styles.stateTextBox}> Bật</Text>
                                    <Switch         
                                        trackColor={{false: '#767577', true: '#81b0ff'}}
                                        thumbColor={isEnabled ? '#f5dd4b' : '#f4f3f4'}
                                        ios_backgroundColor="#3e3e3e"
                                        onValueChange={toggleSwitch}
                                        value={isEnabled}
                                        style={styles.toggleInBox}
                                    />
                                </View>
                            </View>
                        </View>
                    </ScrollView>
                </View>
                <View>
                    
                </View>
            </View>
            {/* footer */}
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
        </View>
    );
}

export default HomeScreen;

const styles = StyleSheet.create({
    container: {
        flex: 1,
        flexDirection: 'column',
        backgroundColor: '#EFF1F5',
    },
    subContainer: {
        flex: 9,
        flexDirection: 'column',
        paddingTop: 20,
        paddingLeft: 20,
        paddingRight: 20,

    },
    // header
    headerWrapper: {
        flex: 1,
        flexDirection: 'row',
        paddingTop: 15,
        justifyContent: 'center',
        alignItems:'center',

    },
    headerTitle: {
        flex: 8,
        // backgroundColor: 'blue',
    },
    headerNotification: {
        flex: 2,
        justifyContent: 'center',
        alignItems: 'center',
    },

    // weather widget
    weatherWidget: {
        flex: 1,
        // backgroundColor: '#5ED9E1',
        marginTop: 20,
    },
    weatherInfor: {
        position: 'absolute',
        flexDirection: 'row',
    },
    locationInfor: {
        flex: 7,
        // position: 'absolute',
        // backgroundColor: '#5ED9E1',
        padding:15
    },
    locationTitle: {
        color: 'white',
        fontFamily: 'Inter-Bold',
        fontSize: 22,

    },
    location: {
        color: '#EBEBF5',
        fontFamily: 'Inter-Regular',
        fontSize: 13,
    },
    weatherStateContainer: {
        flexDirection: 'row',
        // justifyContent: 'space-between',
        alignItems: 'center',
    },
    weatherState: {
        paddingLeft: 10,
        color: 'white',
        fontFamily: 'Inter-Regular',
    },
    weatherTemp: {
        // position: 'absolute',
        flex: 4,
        
        // backgroundColor: 'blue',
        paddingRight: 15,
    },
    tempContainer: {
        flexDirection: 'row',
        paddingBottom: 0,
    },
    tempInfor: {
        fontSize: 48,
        color: 'white',
        fontFamily: 'Inter-Light',
    },
    humidity: {
        fontFamily: 'Inter-Bold',
        color: 'white',
    },
    // Device details
    elementDetail: {
        flex:4 ,
        flexDirection: 'column',
        paddingTop: 15,
        
    },
    roomDetail: {
        alignItems: 'center',
        marginBottom: 10,
        paddingBottom: 10,
        paddingTop: 10,
    },
    roomCell: {
        marginLeft: 15,
        marginRight: 15,
    },
    listDetail: {
        // flexDirection: 'column',
      
    },
    listDetailRow: {
        flexDirection: 'row',
    },
    box: {
        height: 170,
        paddingTop: 15,
        paddingRight: 10,
        paddingLeft: 20,
        margin: 5,
        flex: 1,
        flexDirection: 'column',
        borderRadius: 15,
        backgroundColor: '#33394D',
    },
    iconBox: {
        flex: 1,
    },
    titleBox: {
        fontFamily: 'Inter-Bold',
        fontSize: 18,
        fontWeight: 'bold',
        color: 'white',
        flex: 1
    },
    stateBox: {
        flex: 1,
        justifyContent: 'flex-end',
        alignItems: 'flex-end',
        flexDirection: 'row',
        
    },
    stateTextBox: {
        color: 'white',
        fontFamily: 'Inter-Bold',
        flex: 1,
        paddingBottom: 15,
        fontSize: 17,
    },
    toggleInBox: {
        flex: 1,
    },

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