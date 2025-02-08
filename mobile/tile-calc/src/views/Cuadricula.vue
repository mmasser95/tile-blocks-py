<template>
    <ion-page>
        <Layout title="Cuadricula">
            <div class="v-flex">
                <div class="h-flex">
                    <ion-input label="Area Width (cm)" label-placement="floating" type="number" />
                    <ion-input label="Area Height (cm)" label-placement="floating" type="number" />
                </div>
                <div class="h-flex">
                    <ion-input label="Tile Width (cm)" label-placement="floating" />
                    <ion-input label="Tile Height (cm)" label-placement="floating" />
                </div>
                <v-stage :config="{width:500, height:500}">
                    <v-layer>
                        <v-rect :config="{width:100, height:100, fill:'red'}" />
                    </v-layer>
                </v-stage>
            </div>
        </Layout>
    </ion-page>
</template>
<script lang="ts" setup>
import { IonContent, IonPage, IonInput, IonGrid, IonRow } from '@ionic/vue';
import Layout from '@/components/Layout.vue';
</script>
<style scoped>
.h-flex {
    display: flex;
    justify-content: space-between;
    gap: 5px;
}

.v-flex {
    display: flex;
    justify-content: space-between;
    flex-direction: column;
    gap: 5px;
}
</style>