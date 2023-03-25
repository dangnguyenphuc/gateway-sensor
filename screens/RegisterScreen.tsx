import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';

export default function LogoutScreen({navigation}: {navigation: any}) {
    return (
        <View style={styles.container}>
            <Text> Login Screen </Text>
            <Button 
                title="This is Login Screen"
                onPress={() => navigation.navigate("HomeScreen")}
            />
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center'
    },
});