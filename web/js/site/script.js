class EthFrame {
    constructor(dmac, smac, type, fcs, data) {
        this.dmac = dmac
        this.smac = smac
        this.type = type
        this.fcs = fcs
        this.data = data
    }

    setDmac(new_dmac) {
        this.dmac = new_dmac      
    }

    getDmac() {
        return this.dmac
    }
}

class Switch {
    constructor(port, mac) {
        this.port = port
        this.mac = mac
    }
}


mac1 = {
    1: "AA:AA",
    2: "BB:BB",
    3: "CC:CC",
    4: "DD:DD"
}

const s1 = new Switch(4, mac1)


const f1 = new EthFrame("AA:AA", "BB:BB", "Eth Frame", 123, "SomePacket")
console.log(f1.getDmac())

const f2 = new EthFrame("AA:AA", "CC:CC", "Eth frame", 555, "SomeSecondPacket")
console.log(f1.getDmac())