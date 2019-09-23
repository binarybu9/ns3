#! /usr/bin/env python

# Programs that are runnable.
ns3_runnable_programs = ['build/src/aodv/examples/ns3.20-aodv-debug', 'build/src/bittorrent/examples/ns3.20-bittorrent-no-story-debug', 'build/src/bittorrent/examples/ns3.20-vodsim-debug', 'build/src/bridge/examples/ns3.20-csma-bridge-debug', 'build/src/bridge/examples/ns3.20-csma-bridge-one-hop-debug', 'build/src/buildings/examples/ns3.20-buildings-pathloss-profiler-debug', 'build/src/config-store/examples/ns3.20-config-store-save-debug', 'build/src/core/examples/ns3.20-main-callback-debug', 'build/src/core/examples/ns3.20-sample-simulator-debug', 'build/src/core/examples/ns3.20-main-ptr-debug', 'build/src/core/examples/ns3.20-main-random-variable-debug', 'build/src/core/examples/ns3.20-main-random-variable-stream-debug', 'build/src/core/examples/ns3.20-sample-random-variable-debug', 'build/src/core/examples/ns3.20-sample-random-variable-stream-debug', 'build/src/core/examples/ns3.20-command-line-example-debug', 'build/src/core/examples/ns3.20-hash-example-debug', 'build/src/core/examples/ns3.20-main-test-sync-debug', 'build/src/csma/examples/ns3.20-csma-one-subnet-debug', 'build/src/csma/examples/ns3.20-csma-broadcast-debug', 'build/src/csma/examples/ns3.20-csma-packet-socket-debug', 'build/src/csma/examples/ns3.20-csma-multicast-debug', 'build/src/csma/examples/ns3.20-csma-raw-ip-socket-debug', 'build/src/csma/examples/ns3.20-csma-ping-debug', 'build/src/csma-layout/examples/ns3.20-csma-star-debug', 'build/src/dsdv/examples/ns3.20-dsdv-manet-debug', 'build/src/dsr/examples/ns3.20-dsr-debug', 'build/src/emu/examples/ns3.20-emu-udp-echo-debug', 'build/src/emu/examples/ns3.20-emu-ping-debug', 'build/src/energy/examples/ns3.20-li-ion-energy-source-debug', 'build/src/fd-net-device/examples/ns3.20-dummy-network-debug', 'build/src/fd-net-device/examples/ns3.20-fd2fd-onoff-debug', 'build/src/fd-net-device/examples/ns3.20-realtime-dummy-network-debug', 'build/src/fd-net-device/examples/ns3.20-realtime-fd2fd-onoff-debug', 'build/src/fd-net-device/examples/ns3.20-fd-emu-ping-debug', 'build/src/fd-net-device/examples/ns3.20-fd-emu-udp-echo-debug', 'build/src/fd-net-device/examples/ns3.20-fd-emu-onoff-debug', 'build/src/fd-net-device/examples/ns3.20-fd-tap-ping-debug', 'build/src/fd-net-device/examples/ns3.20-fd-tap-ping6-debug', 'build/src/internet/examples/ns3.20-main-simple-debug', 'build/src/lr-wpan/examples/ns3.20-lr-wpan-packet-print-debug', 'build/src/lr-wpan/examples/ns3.20-lr-wpan-phy-test-debug', 'build/src/lr-wpan/examples/ns3.20-lr-wpan-data-debug', 'build/src/lr-wpan/examples/ns3.20-lr-wpan-error-model-plot-debug', 'build/src/lr-wpan/examples/ns3.20-lr-wpan-error-distance-plot-debug', 'build/src/lte/examples/ns3.20-lena-cqi-threshold-debug', 'build/src/lte/examples/ns3.20-lena-dual-stripe-debug', 'build/src/lte/examples/ns3.20-lena-fading-debug', 'build/src/lte/examples/ns3.20-lena-intercell-interference-debug', 'build/src/lte/examples/ns3.20-lena-pathloss-traces-debug', 'build/src/lte/examples/ns3.20-lena-profiling-debug', 'build/src/lte/examples/ns3.20-lena-rem-debug', 'build/src/lte/examples/ns3.20-lena-rem-sector-antenna-debug', 'build/src/lte/examples/ns3.20-lena-rlc-traces-debug', 'build/src/lte/examples/ns3.20-lena-simple-debug', 'build/src/lte/examples/ns3.20-lena-simple-epc-debug', 'build/src/lte/examples/ns3.20-lena-x2-handover-debug', 'build/src/lte/examples/ns3.20-lena-x2-handover-measures-debug', 'build/src/mesh/examples/ns3.20-mesh-debug', 'build/src/mobility/examples/ns3.20-main-grid-topology-debug', 'build/src/mobility/examples/ns3.20-main-random-topology-debug', 'build/src/mobility/examples/ns3.20-main-random-walk-debug', 'build/src/mobility/examples/ns3.20-mobility-trace-example-debug', 'build/src/mobility/examples/ns3.20-ns2-mobility-trace-debug', 'build/src/mobility/examples/ns3.20-bonnmotion-ns2-example-debug', 'build/src/mpi/examples/ns3.20-simple-distributed-debug', 'build/src/mpi/examples/ns3.20-third-distributed-debug', 'build/src/mpi/examples/ns3.20-nms-p2p-nix-distributed-debug', 'build/src/mpi/examples/ns3.20-simple-distributed-empty-node-debug', 'build/src/netanim/examples/ns3.20-dumbbell-animation-debug', 'build/src/netanim/examples/ns3.20-grid-animation-debug', 'build/src/netanim/examples/ns3.20-star-animation-debug', 'build/src/netanim/examples/ns3.20-wireless-animation-debug', 'build/src/netanim/examples/ns3.20-uan-animation-debug', 'build/src/netanim/examples/ns3.20-dynamic_linknode-debug', 'build/src/netanim/examples/ns3.20-resources_demo-debug', 'build/src/network/examples/ns3.20-main-packet-header-debug', 'build/src/network/examples/ns3.20-main-packet-tag-debug', 'build/src/network/examples/ns3.20-red-tests-debug', 'build/src/network/examples/ns3.20-droptail_vs_red-debug', 'build/src/nix-vector-routing/examples/ns3.20-nix-simple-debug', 'build/src/nix-vector-routing/examples/ns3.20-nms-p2p-nix-debug', 'build/src/olsr/examples/ns3.20-simple-point-to-point-olsr-debug', 'build/src/olsr/examples/ns3.20-olsr-hna-debug', 'build/src/point-to-point/examples/ns3.20-main-attribute-value-debug', 'build/src/propagation/examples/ns3.20-main-propagation-loss-debug', 'build/src/propagation/examples/ns3.20-jakes-propagation-model-example-debug', 'build/src/sixlowpan/examples/ns3.20-example-sixlowpan-debug', 'build/src/sixlowpan/examples/ns3.20-example-ping-lr-wpan-debug', 'build/src/spectrum/examples/ns3.20-adhoc-aloha-ideal-phy-debug', 'build/src/spectrum/examples/ns3.20-adhoc-aloha-ideal-phy-matrix-propagation-loss-model-debug', 'build/src/spectrum/examples/ns3.20-adhoc-aloha-ideal-phy-with-microwave-oven-debug', 'build/src/stats/examples/ns3.20-gnuplot-example-debug', 'build/src/stats/examples/ns3.20-double-probe-example-debug', 'build/src/stats/examples/ns3.20-gnuplot-aggregator-example-debug', 'build/src/stats/examples/ns3.20-gnuplot-helper-example-debug', 'build/src/stats/examples/ns3.20-file-aggregator-example-debug', 'build/src/stats/examples/ns3.20-file-helper-example-debug', 'build/src/tap-bridge/examples/ns3.20-tap-csma-debug', 'build/src/tap-bridge/examples/ns3.20-tap-csma-virtual-machine-debug', 'build/src/tap-bridge/examples/ns3.20-tap-wifi-virtual-machine-debug', 'build/src/tap-bridge/examples/ns3.20-tap-wifi-dumbbell-debug', 'build/src/topology-read/examples/ns3.20-topology-read-debug', 'build/src/uan/examples/ns3.20-uan-cw-example-debug', 'build/src/uan/examples/ns3.20-uan-rc-example-debug', 'build/src/virtual-net-device/examples/ns3.20-virtual-net-device-debug', 'build/src/wave/examples/ns3.20-wave-simple-80211p-debug', 'build/src/wifi/examples/ns3.20-wifi-phy-test-debug', 'build/src/wimax/examples/ns3.20-wimax-ipv4-debug', 'build/src/wimax/examples/ns3.20-wimax-multicast-debug', 'build/src/wimax/examples/ns3.20-wimax-simple-debug', 'build/examples/udp/ns3.20-udp-echo-debug', 'build/examples/tcp/ns3.20-tcp-large-transfer-debug', 'build/examples/tcp/ns3.20-tcp-nsc-lfn-debug', 'build/examples/tcp/ns3.20-tcp-nsc-zoo-debug', 'build/examples/tcp/ns3.20-tcp-star-server-debug', 'build/examples/tcp/ns3.20-star-debug', 'build/examples/tcp/ns3.20-tcp-bulk-send-debug', 'build/examples/tcp/ns3.20-tcp-nsc-comparison-debug', 'build/examples/tcp/ns3.20-tcp-variants-comparison-debug', 'build/examples/wireless/ns3.20-mixed-wireless-debug', 'build/examples/wireless/ns3.20-wifi-adhoc-debug', 'build/examples/wireless/ns3.20-wifi-clear-channel-cmu-debug', 'build/examples/wireless/ns3.20-wifi-ap-debug', 'build/examples/wireless/ns3.20-wifi-wired-bridging-debug', 'build/examples/wireless/ns3.20-simple-wifi-frame-aggregation-debug', 'build/examples/wireless/ns3.20-multirate-debug', 'build/examples/wireless/ns3.20-wifi-simple-adhoc-debug', 'build/examples/wireless/ns3.20-wifi-simple-adhoc-grid-debug', 'build/examples/wireless/ns3.20-wifi-simple-infra-debug', 'build/examples/wireless/ns3.20-wifi-simple-interference-debug', 'build/examples/wireless/ns3.20-wifi-blockack-debug', 'build/examples/wireless/ns3.20-ofdm-validation-debug', 'build/examples/wireless/ns3.20-wifi-hidden-terminal-debug', 'build/examples/wireless/ns3.20-ht-wifi-network-debug', 'build/examples/realtime/ns3.20-realtime-udp-echo-debug', 'build/examples/socket/ns3.20-socket-bound-static-routing-debug', 'build/examples/socket/ns3.20-socket-bound-tcp-static-routing-debug', 'build/examples/socket/ns3.20-socket-options-ipv4-debug', 'build/examples/socket/ns3.20-socket-options-ipv6-debug', 'build/examples/matrix-topology/ns3.20-matrix-topology-debug', 'build/examples/tutorial/ns3.20-hello-simulator-debug', 'build/examples/tutorial/ns3.20-first-debug', 'build/examples/tutorial/ns3.20-second-debug', 'build/examples/tutorial/ns3.20-third-debug', 'build/examples/tutorial/ns3.20-fourth-debug', 'build/examples/tutorial/ns3.20-fifth-debug', 'build/examples/tutorial/ns3.20-sixth-debug', 'build/examples/tutorial/ns3.20-seventh-debug', 'build/examples/routing/ns3.20-dynamic-global-routing-debug', 'build/examples/routing/ns3.20-static-routing-slash32-debug', 'build/examples/routing/ns3.20-global-routing-slash32-debug', 'build/examples/routing/ns3.20-global-injection-slash32-debug', 'build/examples/routing/ns3.20-simple-global-routing-debug', 'build/examples/routing/ns3.20-simple-alternate-routing-debug', 'build/examples/routing/ns3.20-mixed-global-routing-debug', 'build/examples/routing/ns3.20-simple-routing-ping6-debug', 'build/examples/routing/ns3.20-manet-routing-compare-debug', 'build/examples/routing/ns3.20-ripng-simple-network-debug', 'build/examples/naming/ns3.20-object-names-debug', 'build/examples/stats/ns3.20-wifi-example-sim-debug', 'build/examples/ipv6/ns3.20-icmpv6-redirect-debug', 'build/examples/ipv6/ns3.20-ping6-debug', 'build/examples/ipv6/ns3.20-radvd-debug', 'build/examples/ipv6/ns3.20-radvd-two-prefix-debug', 'build/examples/ipv6/ns3.20-test-ipv6-debug', 'build/examples/ipv6/ns3.20-fragmentation-ipv6-debug', 'build/examples/ipv6/ns3.20-fragmentation-ipv6-two-MTU-debug', 'build/examples/ipv6/ns3.20-loose-routing-ipv6-debug', 'build/examples/ipv6/ns3.20-wsn-ping6-debug', 'build/examples/error-model/ns3.20-simple-error-model-debug', 'build/examples/udp-client-server/ns3.20-udp-client-server-debug', 'build/examples/udp-client-server/ns3.20-udp-trace-client-server-debug', 'build/examples/energy/ns3.20-energy-model-example-debug', 'build/scratch/ns3.20-scratch-simulator-debug', 'build/scratch/subdir/ns3.20-subdir-debug']

# Scripts that are runnable.
ns3_runnable_scripts = ['csma-bridge.py', 'sample-simulator.py', 'wifi-olsr-flowmon.py', 'tap-csma-virtual-machine.py', 'tap-wifi-virtual-machine.py', 'mixed-wireless.py', 'wifi-ap.py', 'realtime-udp-echo.py', 'first.py', 'simple-routing-ping6.py']

