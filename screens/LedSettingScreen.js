import React, { useState } from "react";
import {
  View,
  Text,
  Button,
  StyleSheet,
  SafeAreaView,
  Image,
  ScrollView,
  Dimensions,
  TouchableOpacity,
  Modal,
  FlatList,
  PanResponder,
} from "react-native";
import Icon1 from "react-native-vector-icons/MaterialCommunityIcons";
import Icon from "react-native-vector-icons/Ionicons";
import Icon3 from "react-native-vector-icons/FontAwesome";
import Icon2 from "react-native-vector-icons/Feather";
import BottomBar from "../components/BottomBar";
import { StatusBar } from "expo-status-bar";
import { Line, LinearGradient } from "react-native-svg";
import SelectDropdown from "react-native-select-dropdown";

const ScreenWidth = Dimensions.get("window").width;
const ScreenHeight = Dimensions.get("window").height;

const LedSettingScreen = ({ navigation }) => {
  return (
    <View style={styles.Container}>
      <View style={styles.headContainer}>
        <StatusBar barStyle="light-content" />
        <View style={styles.leftHeadContainer}>
          <Icon
            ios="ios-add"
            android="android-add"
            name="chevron-back-circle-outline"
            size={32}
            style={styles.chevronLeft}
          ></Icon>
        </View>
        <View style={styles.middleHeadContainer}>
          <Text style={styles.topTitle}>ĐÈN</Text>
        </View>
        <View style={styles.rightHeadContainer}>
          {/* <Icon
            ios="ios-add"
            android="android-add"
            name="settings-outline"
            size={30}
            style={styles.settingIcon}
          ></Icon> */}
        </View>
      </View>
      <View style={styles.middleContainer}>
        <View style={styles.leftMiddleContainer}></View>
        <View style={styles.centerMiddleContainer}>
          <View style={styles.addDevicesContainer}>
            <Text style={styles.middleTextContainer}>Thêm thiết bị</Text>
            <Icon
              style={styles.chevronForwardIcon}
              ios="ios-add"
              android="android-add"
              name="chevron-forward"
              size={30}
            />
          </View>
          <View style={styles.deleteDevicesContainer}>
            <Text style={styles.middleTextContainer}>Xóa thiết bị</Text>
            <Icon
              style={styles.chevronForwardIcon}
              ios="ios-add"
              android="android-add"
              name="chevron-forward"
              size={30}
            />
          </View>
        </View>
        <View style={styles.rightMiddleContainer}></View>
      </View>
      <View style={styles.bottomContainer}>
        <View style={styles.leftBottomContainer}>
          <Image
            style={styles.leftBottomContainer_Footer}
            source={require("../assets/images/Led_Fan/leftFooter.png")}
          />
          <Icon
            ios="ios-add"
            android="android-add"
            name="home-outline"
            size={30}
            color={"white"}
            style={styles.HomeIcon}
          ></Icon>
        </View>
        <View style={styles.middleBottomContainer}>
          <View style={styles.circleContainer}>
            <Icon3
              style={styles.microphoneIcon}
              name="microphone"
              size={30}
              color="white"
            />
          </View>
        </View>
        <View style={styles.rightBottomContainer}>
          <Image
            style={styles.rightBottomContainer_Footer}
            source={require("../assets/images/Led_Fan/rightFooter.png")}
          ></Image>
          <Icon
            ios="ios-add"
            android="android-add"
            name="person-outline"
            size={30}
            color={"white"}
            style={styles.personIcon}
          ></Icon>
        </View>
      </View>
    </View>
  );
};

export default LedSettingScreen;

const styles = StyleSheet.create({
  Container: {
    flex: 1,
    flexDirection: "column",
  },

  headContainer: {
    flex: 1.2,
    flexDirection: "row",
    backgroundColor: "#EFF1F5",
  },
  leftHeadContainer: {
    flex: 1,
  },
  middleHeadContainer: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
  rightHeadContainer: {
    flex: 1,
  },
  chevronLeft: {
    position: "absolute",
    top: 0.04 * ScreenHeight,
    left: 0.025 * ScreenWidth,
  },
  topTitle: {
    fontWeight: "bold",
    // fontSize: 20,
    fontSize: 0.0525 * ScreenWidth,
    // top: 10,
    top: 0.015 * ScreenHeight,
  },
  settingIcon: {
    position: "absolute",
    top: 0.04 * ScreenHeight,
    right: 0.025 * ScreenWidth,
  },

  middleContainer: {
    flex: 9.65,
    flexDirection: "row",
    backgroundColor: "#EFF1F5",
    justifyContent: "space-around",
  },
  leftMiddleContainer: {
    width: 0.05 * ScreenWidth,
  },
  centerMiddleContainer: {
    width: 0.85 * ScreenWidth,
    // borderWidth: 1,
  },
  rightMiddleContainer: {
    width: 0.05 * ScreenWidth,
  },
  addDevicesContainer: {
    borderBottomWidth: 1,
    height: 0.08 * ScreenHeight,
    borderColor: "rgba(0, 0, 0, 0.3)",
    flexDirection: "row",
    justifyContent: "flex-start",
  },
  deleteDevicesContainer: {
    borderBottomWidth: 1,
    height: 0.08 * ScreenHeight,
    borderColor: "rgba(0, 0, 0, 0.3)",
    flexDirection: "row",
    justifyContent: "flex-start",
  },
  middleTextContainer: {
    fontWeight: 500,
    fontSize: 18,
    color: "#000000",
    width: 0.78 * ScreenWidth,
    bottom: -26,
    // borderWidth: 1,
  },
  chevronForwardIcon: {
    width: 0.1 * ScreenWidth,
    bottom: -20,
    // borderWidth: 1,
  },

  bottomContainer: {
    flex: 1.2,
    flexDirection: "row",
    backgroundColor: "#EFF1F5",
  },
  leftBottomContainer: {
    flex: 1,
  },
  middleBottomContainer: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
  rightBottomContainer: {
    flex: 1,
  },
  leftBottomContainer_Footer: {
    justifyContent: "flex-start",
    width: "100%",
  },
  HomeIcon: {
    position: "absolute",
    bottom: 0.03 * ScreenHeight,
    left: 0.065 * ScreenWidth,
  },
  circleContainer: {
    position: "absolute",
    justifyContent: "center",
    alignItems: "center",
    width: 60,
    height: 60,
    borderRadius: 100 / 2,
    backgroundColor: "green",
  },
  microphoneIcon: {},
  rightBottomContainer_Footer: {
    justifyContent: "flex-start",
    width: "100%",
  },
  personIcon: {
    position: "absolute",
    bottom: 0.03 * ScreenHeight,
    right: 0.065 * ScreenWidth,
  },
});
