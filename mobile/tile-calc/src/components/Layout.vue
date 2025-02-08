<template>
    <ion-header :translucent="true">
        <ion-toolbar>
            <ion-buttons slot="start">
                <ion-menu-button color="primary"></ion-menu-button>
            </ion-buttons>
            <ion-title>{{ title }}</ion-title>
        </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="false">
        <div id="container">
            <ion-grid>
                <ion-row>
                    <ion-col size="12" size-md="4"></ion-col>
                    <ion-col size="12" size-md="8">
                        <slot></slot>
                    </ion-col>
                    <ion-col size="12" size-md="4"></ion-col>
                </ion-row>
            </ion-grid>
        </div>
    </ion-content>
</template>

<script lang="ts" setup>
import { IonGrid, IonRow, IonCol, IonHeader, IonToolbar, IonButtons, IonTitle, IonContent, IonMenuButton } from '@ionic/vue';

defineProps<{
    title: string
}>()
</script>

<style scoped>
#container {
    text-align: center;
    position: absolute;
    left: 0;
    right: 0;
    top: 50%;
    transform: translateY(-50%);
}

#container strong {
    font-size: 20px;
    line-height: 26px;
}

#container p {
    font-size: 16px;
    line-height: 22px;
    color: #8c8c8c;
    margin: 0;
}

#container a {
    text-decoration: none;
}
</style>