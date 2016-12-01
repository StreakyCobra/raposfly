import BigNumber from 'bignumber.js'

var format = {
    decimalSeparator: '.',
    groupSeparator: '\'',
    groupSize: 3,
    secondaryGroupSize: 0,
    fractionGroupSeparator: ' ',
    fractionGroupSize: 0
}
BigNumber.config({ FORMAT: format })

export default BigNumber
