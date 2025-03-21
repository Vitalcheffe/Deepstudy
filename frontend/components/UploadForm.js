import React, { useState } from 'react';
import { View, Button, StyleSheet } from 'react-native';

export default function UploadForm({ onUpload }) {
  const [file, setFile] = useState(null);

  const handleUpload = () => {
    if (file) {
      onUpload(file);
    }
  };

  return (
    <View style={styles.form}>
      <Button title="Télécharger un fichier" onPress={handleUpload} />
    </View>
  );
}
const styles = StyleSheet.create({
  form: {
    marginTop: 20,
  },
});

