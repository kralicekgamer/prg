class EthFrame {
    constructor(dmac, smac, type, fcs, data) {
        this.dmac = dmac;
        this.smac = smac;
        this.type = type;
        this.fcs = fcs;
        this.data = data;
    }

    setDmac(new_dmac) {
        this.dmac = new_dmac;      
    }

    getDmac() {
        return this.dmac;
    }
}

const f1 = new EthFrame("AA:AA", "BB:BB", "Eth Frame", 123, "SomePacket");
console.log(f1.getDmac());