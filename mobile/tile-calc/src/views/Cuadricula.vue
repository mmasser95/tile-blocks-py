<template>
    <ion-page>
        <Layout title="Cuadricula">
            <div class="v-flex">
                <div class="h-flex">
                    <ion-input label="Area Width (cm)" label-placement="floating" type="number" v-model="areaWidth" />
                    <ion-input label="Area Height (cm)" label-placement="floating" type="number" v-model="areaHeight" />
                </div>
                <div class="h-flex">
                    <ion-input label="Tile Width (cm)" label-placement="floating" type="number" v-model="tileWidth" />
                    <ion-input label="Tile Height (cm)" label-placement="floating" type="number" v-model="tileHeight" />
                </div>
                <v-stage :config="stageConfig">
                    <v-layer>
                        <v-rect v-for="(tile, index) in tiles" :key="index" :config="{
                            x: tile.x,
                            y: tile.y,
                            width: tile.w,
                            height: tile.h,
                            fill: tile.complete ? 'lightblue' : 'red',
                            stroke: 'black'
                        }" @click="showTileInfo(tile)" />
                    </v-layer>
                </v-stage>
            </div>
            <div v-if="tileInfo" class="tile-info">
                <p><strong>Medidas de la baldosa:</strong></p>
                <p>Ancho: {{ tileInfo.w }}cm</p>
                <p>Alto: {{ tileInfo.h }}cm</p>
                <p>X: {{ tileInfo.x }}cm</p>
                <p>Y: {{ tileInfo.y }}cm</p>
            </div>
        </Layout>
    </ion-page>
</template>
<script lang="ts" setup>
import { IonContent, IonPage, IonInput, IonGrid, IonRow } from '@ionic/vue';
import Layout from '@/components/Layout.vue';
import { ref } from 'vue';

const areaWidth = ref(150);
const areaHeight = ref(170)
const tileWidth = ref(20)
const tileHeight = ref(30)

type Tile = {
    x: number,
    y: number,
    w: number,
    h: number,
    complete: boolean
}
const tiles = ref<Tile[]>([])

const tileInfo = ref<Tile>()

const stageConfig=ref({
    width:window.innerWidth,
    height:window.innerHeight/4 + window.innerHeight/3
})

const calcTiles = () => {
    const tiles_x = Math.ceil(areaWidth.value / tileWidth.value)
    const tiles_y = Math.ceil(areaHeight.value / tileHeight.value)
    let result = []
    for (let i = 0; i < tiles_x; i++) {
        for (let j = 0; j < tiles_y; j++) {
            let x = i * tileWidth.value
            let y = j * tileHeight.value

            let w = tileWidth.value
            let h = tileHeight.value

            if (x + w > areaWidth.value) {
                w = areaWidth.value - x
            }
            if (y + h > areaHeight.value) {
                h = areaHeight.value - y
            }

            result.push({ x, y, w, h, complete: w == tileWidth.value && h == tileHeight.value })
        }
    }
    tiles.value = result
}

const showTileInfo = (tile: Tile) => {
    tileInfo.value = tile
}

calcTiles()

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