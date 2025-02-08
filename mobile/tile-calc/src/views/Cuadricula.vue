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
                <div class="h-flex">
                    <p>Desperdicio X: {{ spareX }}x{{ spareY }} cm</p>
                    <p>Baldosas (enteras): {{ complete_x }}x{{ complete_y }}</p>
                    <p>Baldosas (todas): {{ tilesX }}x{{ tilesY }}</p>
                </div>
                <v-stage ref="stage" :config="stageConfig">
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
            <div v-if="tileInfo" class="h-flex">
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
import { ref, watch } from 'vue';

const areaWidth = ref(150);
const areaHeight = ref(170)
const tileWidth = ref(20)
const tileHeight = ref(30)

const spareX = ref(0)
const spareY = ref(0)

const complete_x = ref(0)
const complete_y = ref(0)

const tilesX = ref(0)
const tilesY = ref(0)
const stage = ref()

type Tile = {
    x: number,
    y: number,
    w: number,
    h: number,
    complete: boolean
}
const tiles = ref<Tile[]>([])

const tileInfo = ref<Tile>()

const stageConfig = ref({
    width: window.innerWidth,
    height: window.innerHeight / 4 + window.innerHeight / 3
})

const calcTiles = () => {
    const tiles_x = Math.ceil(areaWidth.value / tileWidth.value)
    const tiles_y = Math.ceil(areaHeight.value / tileHeight.value)
    tilesX.value = tiles_x
    tilesY.value = tiles_y
    spareX.value = areaWidth.value % tileWidth.value
    spareY.value = areaHeight.value % tileHeight.value
    complete_y.value = Math.floor(areaHeight.value / tileHeight.value)
    complete_x.value = Math.floor(areaWidth.value / tileWidth.value)
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
    stageConfig.value = {
        width: tiles_x * tileWidth.value,
        height: tiles_y * tileHeight.value,
    };
}

const showTileInfo = (tile: Tile) => {
    tileInfo.value = tile
}



calcTiles()

watch(areaHeight, () => calcTiles())
watch(areaWidth, () => calcTiles())
watch(tileHeight, () => {
    //@ts-ignore
    tileHeight.value = parseInt(tileHeight.value)
    calcTiles()
})
watch(tileWidth, () => {
    //@ts-ignore
    tileWidth.value = parseInt(tileWidth.value)
    calcTiles()
})

</script>
<style scoped>
.h-flex {
    display: flex;
    justify-content: space-between;
    gap: 10px;
}

.v-flex {
    display: flex;
    justify-content: space-between;
    flex-direction: column;
    gap: 5px;
}
</style>